import os
import sys
import json
import urllib.request
import urllib.error
import subprocess
from datetime import datetime

def get_git_diff():
    try:
        # Check if HEAD~1 exists
        subprocess.check_call(["git", "rev-parse", "--verify", "HEAD~1"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        diff = subprocess.check_output(["git", "diff", "HEAD~1", "HEAD"], text=True, errors="replace")
        return diff
    except Exception:
        try:
            return subprocess.check_output(["git", "show", "--stat", "-p"], text=True, errors="replace")
        except Exception:
            return "Diff bilgisi alınamadı."

def read_prompt_file():
    if os.path.exists("prompt.md"):
        try:
            with open("prompt.md", "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception as e:
            return f"(prompt.md okuma hatası: {e})"
    return ""

def call_gemini(api_key, user_input, commit_msg, diff_content):
    # Using Google Gemini API endpoint (gemini-2.5-flash or gemini-1.5-flash)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    system_instruction = (
        "Sen bu GitHub reposunda çalışan yardımcı bir yapay zeka asistanısın. "
        "Kullanıcı her commit attığında veya prompt.md dosyasını güncellediğinde bu istek sana iletilir. "
        "Kullanıcının commit mesajını, prompt.md dosyasındaki içeriğini ve kod değişikliklerini (diff) incele. "
        "Kapsamlı, anlaşılır ve yapıcı bir yanıt ver. "
        "Eğer kullanıcı mobil uygulama geliştirme (Flutter, React Native, Swift, Kotlin vb.) ile ilgili kodlar veya sorular yazmışsa, "
        "en iyi mobil mimari pratiklerini, kod örneklerini ve açıklamalarını sun."
    )

    full_prompt = (
        f"{system_instruction}\n\n"
        f"--- KULLANICI DETAYLARI ---\n"
        f"Commit Mesajı: {commit_msg}\n\n"
    )

    if user_input:
        full_prompt += f"Prompt Dosyası İçeriği (prompt.md):\n```markdown\n{user_input}\n```\n\n"

    # Truncate diff if it's too huge to prevent payload overflow
    if diff_content:
        max_diff_len = 8000
        truncated_diff = diff_content[:max_diff_len] + ("\n... [Diff çok uzun olduğu için kısaltıldı]" if len(diff_content) > max_diff_len else "")
        full_prompt += f"Git Değişiklikleri (Diff):\n```diff\n{truncated_diff}\n```\n"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": full_prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 4096
        }
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            try:
                reply = res_data["candidates"][0]["content"]["parts"][0]["text"]
                return reply
            except (KeyError, IndexError):
                return f"Gemini'den beklenmeyen yanıt formatı:\n```json\n{json.dumps(res_data, indent=2)}\n```"
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        return f"Gemini API Hatası ({e.code}): {error_body}"
    except Exception as e:
        return f"Bağlantı hatası: {str(e)}"

def main():
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    commit_msg = os.environ.get("COMMIT_MSG", "Otomatik commit").strip()

    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    if not api_key:
        error_msg = (
            f"### ⚠️ Gemini API Anahtarı Bulunamadı\n\n"
            f"Tarih: {now_str}\n\n"
            f"Gemini'nin commitlerinize otomatik yanıt verebilmesi için GitHub Secret eklemeniz gerekmektedir:\n\n"
            f"1. GitHub repo sayfanızda **Settings** > **Secrets and variables** > **Actions** bölümüne gidin.\n"
            f"2. **New repository secret** butonuna tıklayın.\n"
            f"3. Name: `GEMINI_API_KEY`\n"
            f"4. Secret: [Google AI Studio](https://aistudio.google.com/app/apikey) adresinden aldığınız Gemini API anahtarını yapıştırın.\n"
            f"5. **Add secret** ile kaydedin ve tekrar bir commit atın!"
        )
        with open("response.md", "w", encoding="utf-8") as f:
            f.write(error_msg + "\n")
        print("GEMINI_API_KEY bulunamadı, uyarı response.md dosyasına yazıldı.")
        return

    prompt_content = read_prompt_file()
    diff_content = get_git_diff()

    print("Gemini API çağrılıyor...")
    gemini_reply = call_gemini(api_key, prompt_content, commit_msg, diff_content)

    # 1. response.md dosyasını en son yanıtla güncelle
    response_header = (
        f"# 🤖 Gemini Yanıtı\n\n"
        f"> **Tarih:** {now_str}  \n"
        f"> **Tetikleyen Commit:** `{commit_msg}`\n\n"
        f"---\n\n"
    )
    with open("response.md", "w", encoding="utf-8") as f:
        f.write(response_header + gemini_reply + "\n")

    # 2. chat_history.md dosyasına geçmiş olarak ekle
    history_entry = (
        f"\n## 📌 Commit: `{commit_msg}` ({now_str})\n\n"
        f"{gemini_reply}\n\n"
        f"---\n"
    )
    with open("chat_history.md", "a", encoding="utf-8") as f:
        f.write(history_entry)

    print("Gemini yanıtı başarıyla response.md ve chat_history.md dosyalarına yazıldı.")

if __name__ == "__main__":
    main()
