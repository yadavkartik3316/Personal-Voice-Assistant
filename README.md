# 🎙️ Personal Voice Assistant — Jarvis

A Python-based personal voice assistant that recognizes voice commands and automates daily tasks. Built as a portfolio project for a third-year engineering student.

---

## 📁 Project Structure

```
Voice Assistant/
├── main.py          # Entry point — starts the assistant and routes commands
├── assistant.py     # VoiceAssistant class — handles speech input and output
├── commands.py      # All feature logic (weather, jokes, search, reminders, etc.)
├── config.py        # App paths, website URLs, and environment variable loading
├── .env             # API keys (not committed to version control)
├── requirements.txt # Python dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> **Note for PyAudio on Windows:** If `pip install pyaudio` fails, download the matching `.whl` from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually:
> ```bash
> pip install PyAudio‑0.2.11‑cp311‑cp311‑win_amd64.whl
> ```

### 4. Configure your API key
Open `.env` and replace the placeholder with your real key:
```
OPENWEATHER_API_KEY=your_actual_key_here
DEFAULT_CITY=YourCity
```
Get a free key at [https://openweathermap.org/api](https://openweathermap.org/api).

### 5. Run the assistant
```bash
python main.py
```

---

## 📦 Libraries Used

| Library            | Purpose                              |
|--------------------|--------------------------------------|
| `SpeechRecognition`| Convert microphone audio to text     |
| `pyttsx3`          | Text-to-speech (offline)             |
| `pyaudio`          | Microphone audio capture             |
| `requests`         | HTTP requests for weather API        |
| `pywhatkit`        | YouTube search and playback          |
| `pyjokes`          | Random programming jokes             |
| `python-dotenv`    | Load API keys from `.env` file       |
| `webbrowser`       | Open URLs in the default browser     |
| `os`               | Launch desktop applications          |
| `datetime`         | Current date and time                |

---

## 🗣️ Available Voice Commands

| What to Say                              | Action                          |
|------------------------------------------|---------------------------------|
| "What's the time?" / "What's the date?" | Tells current date and time     |
| "Weather in London"                      | Fetches live weather            |
| "Tell me a joke"                         | Tells a random joke             |
| "Remind me at 14:30 to drink water"      | Sets a reminder                 |
| "Play Believer on YouTube"               | Plays video on YouTube          |
| "Search Python tutorials"                | Google search                   |
| "Open Gmail"                             | Opens Gmail in browser          |
| "Open GitHub"                            | Opens GitHub in browser         |
| "Open LinkedIn"                          | Opens LinkedIn in browser       |
| "Open Chrome"                            | Launches Chrome                 |
| "Open VS Code"                           | Launches VS Code                |
| "Open Notepad"                           | Launches Notepad                |
| "Open Calculator"                        | Launches Calculator             |
| "Exit" / "Bye" / "Quit"                 | Shuts down the assistant        |

---

## 🔑 Getting an OpenWeatherMap API Key

1. Go to [https://openweathermap.org](https://openweathermap.org) and create a free account.
2. Navigate to **API Keys** in your profile.
3. Copy the key and paste it into your `.env` file.

---

## 💡 Notes

- Requires an active internet connection for speech recognition and weather.
- Reminder times must be in **24-hour HH:MM format** (e.g., "14:30").
- Application paths in `config.py` are set for a standard Windows installation. Update them if your paths differ.

---

## 👤 Author

Built by [Your Name] — Third Year Engineering Student  
[GitHub](https://github.com/your-username) | [LinkedIn](https://linkedin.com/in/your-profile)
