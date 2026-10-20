# 💻 Mobile & Web Development — Lecture Codes & Practice Lab
*Interactive Coding Workspace & Gemini Assistant*

This page is dedicated to hands-on coding exercises, component experiments, and automated code generation.
Whenever you edit the prompt section below and commit, Gemini will analyze your request and write the response (beginner-friendly HTML/CSS/JS or mobile UI code) directly back into this file!

---

## 📚 Starter Example: Beginner-Friendly Mobile Card Layout (HTML & CSS)

A simple, beginner-friendly component demonstrating a clean mobile viewport layout:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mobile Profile Card</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f2f5;
      display: flex;
      justify-content: center;
      padding: 20px;
    }
    .mobile-frame {
      width: 320px;
      background-color: #ffffff;
      border: 1px solid #ddd;
      border-radius: 16px;
      padding: 16px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .profile-title {
      font-size: 18px;
      color: #333;
      margin-bottom: 8px;
    }
    .status-badge {
      display: inline-block;
      padding: 4px 8px;
      background-color: #e8f5e9;
      color: #2e7d32;
      border-radius: 8px;
      font-size: 12px;
    }
    .action-btn {
      width: 100%;
      margin-top: 14px;
      padding: 10px;
      background-color: #1976d2;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="mobile-frame">
    <div class="status-badge">Active Student</div>
    <h2 class="profile-title">Mobile App Development - Week 1-6</h2>
    <p style="font-size: 14px; color: #666;">Ready to test HTML & mobile UI prompts!</p>
    <button class="action-btn">Run Demo</button>
  </div>
</body>
</html>
```

---

## 💬 Student Prompt & Code Request
<!-- Write your prompt, question, or code request below and commit -->
Please write a simple beginner-friendly HTML and CSS login screen designed for a mobile phone view with basic input fields and a submit button.

---

## 🤖 Gemini Response & Generated Code
*(On your commit, Gemini will generate clean, beginner-level HTML/CSS and mobile layout code and append its response right here.)*
