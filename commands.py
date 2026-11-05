import os
import webbrowser
import datetime
import threading

from google import genai

from config import APP_PATHS, WEBSITES, GEMINI_API_KEY

# Configure Gemini once at import time
_client = genai.Client(api_key=GEMINI_API_KEY)

# Stores active reminders as a list of (time_str, message) tuples
_reminders: list[tuple[str, str]] = []


# ── Gemini (general AI responses) ─────────────────────────────────────────────




# ── Gemini (general AI responses) ────────────────────────────────────────────

def ask_gemini(prompt: str) -> str:
    """Send any question to Gemini and return a short spoken-friendly answer."""
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return "Gemini API key is not configured. Please add it to the .env file."
    try:
        system = "You are Jarvis, a helpful voice assistant. Reply in 2-3 short sentences, no markdown."
        response = _client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=f"{system}\n\nUser: {prompt}"
        )
        return response.text.strip()
    except Exception as e:
        return f"Gemini could not respond: {e}"


# ── Applications ──────────────────────────────────────────────────────────────

def open_application(app_name: str) -> str:
    """Open a desktop application by name."""
    path = APP_PATHS.get(app_name.lower())
    if path:
        os.startfile(path)
        return f"Opening {app_name}."
    return f"Sorry, I don't know how to open {app_name}."


# ── Websites ──────────────────────────────────────────────────────────────────

def open_website(site_name: str) -> str:
    """Open a predefined website by name."""
    url = WEBSITES.get(site_name.lower())
    if url:
        webbrowser.open(url)
        return f"Opening {site_name}."
    return f"Sorry, I don't have {site_name} in my list."


# ── Search ────────────────────────────────────────────────────────────────────

def google_search(query: str) -> str:
    """Perform a Google search."""
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for {query}."


def youtube_search(query: str) -> str:
    """Open a YouTube search in the browser."""
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    return f"Searching YouTube for {query}."


# ── Date & Time ───────────────────────────────────────────────────────────────

def get_datetime() -> str:
    """Return the current date and time as a readable string."""
    now = datetime.datetime.now()
    return now.strftime("Today is %A, %B %d %Y. The time is %I:%M %p.")


# ── Reminders ─────────────────────────────────────────────────────────────────

def set_reminder(reminder_time: str, message: str, speak_callback) -> str:
    """
    Set a reminder that fires at reminder_time (HH:MM, 24-hour format).
    speak_callback is the assistant's speak() method used to announce the reminder.
    """
    _reminders.append((reminder_time, message))

    def _wait_and_remind():
        while True:
            if datetime.datetime.now().strftime("%H:%M") == reminder_time:
                speak_callback(f"Reminder: {message}")
                _reminders.remove((reminder_time, message))
                break
            threading.Event().wait(30)

    threading.Thread(target=_wait_and_remind, daemon=True).start()
    return f"Reminder set for {reminder_time}: {message}."
