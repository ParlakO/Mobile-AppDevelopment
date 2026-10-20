# 💻 Mobile & Web Development — Lecture Codes & Practice Lab
*Interactive Coding Workspace & Gemini Assistant*

This page is dedicated to hands-on coding exercises, component experiments, and automated code generation.
Whenever you edit the prompt section below and commit, Gemini will analyze your request and write the response (beginner-friendly HTML/CSS/JS or mobile UI code) directly back into this file!

---

## 📚 Starter Example: Beginner-Friendly Mobile Card Layout (HTML & CSS)

A simple, beginner-friendly component demonstrating a clean mobile viewport layout:

`html
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
`

---

## 💬 Student Prompt & Code Request
<!-- Write your prompt, question, or code request below and commit -->
Can you write a beginner-friendly HTML and CSS code for a simple mobile phone login screen? Keep the design basic and clean with email, password fields, and a login button.

---

## 🤖 Gemini Response & Generated Code

> ⏱️ **Generated at:** 2026-10-20 14:55:42 UTC  
> 📌 **In response to commit:** `Request beginner mobile login screen code from Gemini`

Hello! It’s great to see you working on mobile layouts. A mobile login screen is a perfect project for understanding how to center content and style form inputs for a touch-based device.

Below is a clean, responsive template. I’ve used basic CSS to ensure the layout looks good on a mobile screen.

### Mobile Login Screen

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- This meta tag is crucial for mobile: it makes the page width match the device width -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mobile Login</title>
  <style>
    /* Basic reset to remove default margins */
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: sans-serif; }

    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f9;
    }

    .login-container {
      width: 90%; /* Responsive width */
      max-width: 400px;
      padding: 20px;
      background: white;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    h2 { text-align: center; margin-bottom: 20px; color: #333; }

    /* Styling inputs to be touch-friendly */
    input {
      width: 100%;
      padding: 12px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px; /* Prevents auto-zoom on iOS when typing */
    }

    button {
      width: 100%;
      padding: 12px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover { background-color: #0056b3; }
  </style>
</head>
<body>

  <div class="login-container">
    <h2>Login</h2>
    <form>
      <input type="email" placeholder="Email" required>
      <input type="password" placeholder="Password" required>
      <button type="submit">Log In</button>
    </form>
  </div>

</body>
</html>
```

### Key Educational Notes:

1.  **The Meta Viewport Tag:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">` is the most important line here. Without it, mobile browsers might try to display the page as if it were on a desktop, leading to tiny, unreadable text.
2.  **Flexbox for Centering:** I used `display: flex; justify-content: center; align-items: center;` on the `body`. This is the modern, easiest way to perfectly center a login box in the middle of a screen.
3.  **Touch-Friendly Inputs:** Notice I set the input font size to `16px`. On many mobile devices, if the font size of an input field is smaller than 16px, the browser will automatically zoom in when you tap the field to type, which can be annoying for users.
4.  **Responsive Width:** By setting `width: 90%` and `max-width: 400px`, the box will look great on small phones (taking up most of the screen) but won't get too wide if the user opens the link on a tablet or desktop browser.

Let me know if you’d like to add some JavaScript validation to this form next!

---
