import os
from dotenv import load_dotenv

load_dotenv()

# --- API Keys ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Desktop Application Paths (Windows) ---
APP_PATHS = {
    "chrome":     r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode":     r"C:\Users\{}\AppData\Local\Programs\Microsoft VS Code\Code.exe".format(os.getenv("USERNAME")),
    "notepad":    "notepad.exe",
    "calculator": "calc.exe",
}

# --- Common Websites ---
WEBSITES = {
    "gmail":    "https://mail.google.com",
    "github":   "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "youtube":  "https://www.youtube.com",
    "google":   "https://www.google.com",
}
