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
                return f.read()
        except Exception as e:
            return f"Error reading {TARGET_FILE}: {e}"
    return ""

def extract_prompt_from_content(content):
    marker = "## 💬 Student Prompt & Code Request"
    if marker in content:
        after_marker = content.split(marker)[1]
        response_marker = "## 🤖 Gemini Response & Generated Code"
        if response_marker in after_marker:
            prompt_section = after_marker.split(response_marker)[0]
        else:
            prompt_section = after_marker
        lines = [line.strip() for line in prompt_section.split("\n") if line.strip() and not line.strip().startswith("<!--")]
        return "\n".join(lines)
    return content

def call_gemini(api_key, user_prompt, commit_msg, diff_content):
    models = ["gemini-3.5-flash", "gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.1-flash-lite"]
    
    system_instruction = (
        "You are an expert AI teaching assistant for a student learning Mobile & Web App Development. "
        "The student will submit prompts, code requests, and questions inside their lecturecodes.md file.\n"
        "RULES FOR YOUR RESPONSE:\n"
        "1. When the student asks you to write code, provide clean, beginner-friendly HTML, CSS, and JavaScript "
        "(or basic mobile layouts). The appearance should be simple, clean, entry-level, and easy to understand.\n"
        "2. Avoid overwhelming the student with overly complex libraries, complex build tools, or dense enterprise code.\n"
        "3. Provide clear, supportive, educational explanations of how the code works.\n"
        "4. Format your code cleanly in markdown code blocks with comments explaining each part."
    )

    full_text = (
        f"{system_instruction}\n\n"
        f"--- STUDENT REQUEST CONTEXT ---\n"
        f"Commit Message: {commit_msg}\n\n"
        f"Student Prompt / Request:\n{user_prompt}\n\n"
    )

    if diff_content:
        max_diff = 6000
        truncated_diff = diff_content[:max_diff]
        full_text += f"Recent Git Diff in {TARGET_FILE}:\n```diff\n{truncated_diff}\n```\n"

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
            with urllib.request.urlopen(req, timeout=75) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                reply = res_data["candidates"][0]["content"]["parts"][0]["text"]
                return reply
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8", errors="replace")
            last_error = f"HTTP {e.code} on {model}: {err_msg}"
            print(f"Warning: {model} failed with {last_error}, trying next model...")
            continue
        except Exception as e:
            last_error = f"Error on {model}: {str(e)}"
            print(f"Warning: {model} exception: {last_error}, trying next model...")
            continue

    return f"⚠️ Unable to reach Gemini API after trying multiple models.\nDetails: {last_error}"

def update_lecturecodes_file(full_content, gemini_reply, commit_msg, now_str):
    response_section_header = "## 🤖 Gemini Response & Generated Code"
    
    new_response_block = (
        f"{response_section_header}\n\n"
        f"> ⏱️ **Generated at:** {now_str}  \n"
        f"> 📌 **In response to commit:** `{commit_msg}`\n\n"
        f"{gemini_reply}\n\n"
        f"---\n"
    )

    if response_section_header in full_content:
        # Keep everything before response_section_header, and replace/append the new response
        prefix = full_content.split(response_section_header)[0]
        updated_content = prefix.rstrip() + "\n\n" + new_response_block
    else:
        updated_content = full_content.rstrip() + "\n\n---\n\n" + new_response_block

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

def main():
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    commit_msg = os.environ.get("COMMIT_MSG", "Update code and prompt").strip()
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    if not os.path.exists(TARGET_FILE):
        print(f"Error: {TARGET_FILE} not found!")
        sys.exit(0)

    full_content = read_target_content()

    if not api_key:
        error_msg = (
            "⚠️ **Missing `GEMINI_API_KEY` Secret!**\n\n"
            "To enable automatic Gemini code responses on commit:\n"
            "1. Go to repository **Settings > Secrets and variables > Actions**\n"
            "2. Add a new secret named `GEMINI_API_KEY` with your Gemini API Key.\n"
            "3. Make a commit in `lecturecodes.md` to trigger the assistant!"
        )
        update_lecturecodes_file(full_content, error_msg, commit_msg, now_str)
        print("GEMINI_API_KEY is not set.")
        return

    full_content = read_target_content()
    user_prompt = extract_prompt_from_content(full_content)
    diff_content = get_git_diff()

    print(f"Prompt extracted: {user_prompt[:120]}...")
    print("Calling Gemini API...")

    gemini_reply = call_gemini(api_key, user_prompt, commit_msg, diff_content)
    update_lecturecodes_file(full_content, gemini_reply, commit_msg, now_str)
    print(f"Successfully updated {TARGET_FILE} with Gemini response!")

if __name__ == "__main__":
    main()
