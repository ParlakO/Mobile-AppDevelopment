import os
import sys
import json
import urllib.request
import urllib.error
import subprocess
from datetime import datetime

TARGET_FILE = "lecturecodes.md"

def get_git_diff():
    try:
        subprocess.check_call(["git", "rev-parse", "--verify", "HEAD~1"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        diff = subprocess.check_output(["git", "diff", "HEAD~1", "HEAD", "--", TARGET_FILE], text=True, errors="replace")
        if not diff:
            diff = subprocess.check_output(["git", "diff", "HEAD~1", "HEAD"], text=True, errors="replace")
        return diff
    except Exception:
        try:
            return subprocess.check_output(["git", "show", "--stat", "-p"], text=True, errors="replace")
        except Exception:
            return ""

def read_target_content():
    if os.path.exists(TARGET_FILE):
        try:
            with open(TARGET_FILE, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception as e:
            return f"Error reading {TARGET_FILE}: {e}"
    return ""

def call_gemini(api_key, user_input, commit_msg, diff_content):
    # Fastest model first: gemini-3.1-flash-lite (lowest latency), then gemini-3.5-flash
    models = ["gemini-3.1-flash-lite", "gemini-3.5-flash", "gemini-3.8-flash"]
    
    system_instruction = (
        "You are an assistant for a student studying Mobile and Web Development. "
        "The student will write questions, code prompts, or requests directly in their file. "
        "RULES FOR YOUR RESPONSE:\n"
        "1. When the student asks for code, generate clean, beginner-friendly HTML, CSS, JavaScript, or mobile UI code. "
        "Keep the styling and layout simple, entry-level, clean, and easily understandable for a beginner.\n"
        "2. Keep explanations concise, clear, and focused on how the code works.\n"
        "3. Provide direct code blocks with helpful comments."
    )

    prompt_parts = [system_instruction, ""]
    if commit_msg:
        prompt_parts.append(f"Commit Message: {commit_msg}")
    if user_input:
        prompt_parts.append(f"Student Input in {TARGET_FILE}:\n{user_input}")
    elif diff_content:
        prompt_parts.append(f"Student Changes (Diff):\n```diff\n{diff_content[:4000]}\n```")
    else:
        prompt_parts.append("The student made a commit to request code assistance.")

    full_text = "\n\n".join(prompt_parts)

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": full_text}
                ]
            }
        ]
    }

    last_error = ""
    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1/models/{model}:generateContent?key={api_key}"
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                reply = res_data["candidates"][0]["content"]["parts"][0]["text"]
                return reply
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8", errors="replace")
            last_error = f"HTTP {e.code} on {model}: {err_msg}"
            print(f"Model {model} failed, trying next...")
            continue
        except Exception as e:
            last_error = f"Error on {model}: {str(e)}"
            print(f"Model {model} error: {last_error}, trying next...")
            continue

    return f"⚠️ Gemini API Error: {last_error}"

def update_file(original_content, gemini_reply, now_str):
    if original_content:
        updated = f"{original_content}\n\n---\n\n### 🤖 Gemini Response ({now_str})\n\n{gemini_reply}\n"
    else:
        updated = f"# 🤖 Gemini Response ({now_str})\n\n{gemini_reply}\n"

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(updated)

def main():
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    commit_msg = os.environ.get("COMMIT_MSG", "Update lecturecodes").strip()
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    if not api_key:
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write("⚠️ Missing GEMINI_API_KEY secret in repository settings.\n")
        return

    content = read_target_content()
    diff = get_git_diff()

    print("Calling Gemini API...")
    reply = call_gemini(api_key, content, commit_msg, diff)
    update_file(content, reply, now_str)
    print("Done! Response written to " + TARGET_FILE)

if __name__ == "__main__":
    main()
