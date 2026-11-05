import pyttsx3
import speech_recognition as sr


class VoiceAssistant:
    """Handles text-to-speech output and speech-to-text input."""

    def __init__(self, name: str = "Jarvis"):
        self.name = name
        self._engine = pyttsx3.init()
        self._engine.setProperty("rate", 200)   # speaking speed
        self._engine.setProperty("volume", 1.0)
        self._recognizer = sr.Recognizer()
        self._recognizer.pause_threshold = 1     # seconds of silence before phrase ends

    # ── Output ────────────────────────────────────────────────────────────────

    def speak(self, text: str) -> None:
        """Convert text to speech and print it."""
        print(f"{self.name}: {text}")
        self._engine.say(text)
        self._engine.runAndWait()

    # ── Input ─────────────────────────────────────────────────────────────────

    def listen(self) -> str | None:
        """
        Listen for a voice command and return it as lowercase text.
        Returns None if nothing was understood or an error occurred.
        """
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise before capturing
            self._recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self._recognizer.listen(source, timeout=5, phrase_time_limit=8)
            except sr.WaitTimeoutError:
                return None

        try:
            command = self._recognizer.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that. Could you repeat?")
            return None
        except sr.RequestError:
            self.speak("Speech recognition service is unavailable. Check your internet.")
            return None
        except OSError:
            self.speak("Microphone not detected. Please check your audio input device.")
            return None
