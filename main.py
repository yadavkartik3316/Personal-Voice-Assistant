from assistant import VoiceAssistant
import commands

assistant = VoiceAssistant(name="Jarvis")


def route_command(command: str) -> bool:
    """
    Match a voice command string to the appropriate feature.
    Returns False when the user wants to exit, True otherwise.
    """

    # ── Exit ──────────────────────────────────────────────────────────────────
    if any(word in command for word in ("exit", "quit", "bye", "goodbye")):
        assistant.speak("Goodbye! Have a great day.")
        return False

    # ── Date & Time ───────────────────────────────────────────────────────────
    elif any(word in command for word in ("time", "date", "day")):
        assistant.speak(commands.get_datetime())

    # ── Reminder ──────────────────────────────────────────────────────────────
    elif "remind" in command:
        # Expected phrase: "remind me at HH:MM to <message>"
        try:
            time_part = command.split("at")[1].split("to")[0].strip()
            message_part = command.split("to", 2)[-1].strip()
            assistant.speak(commands.set_reminder(time_part, message_part, assistant.speak))
        except IndexError:
            assistant.speak("Please say: remind me at HH:MM to do something.")

    # ── YouTube ───────────────────────────────────────────────────────────────
    elif "play" in command:
        query = command.replace("play", "").replace("on youtube", "").strip()
        assistant.speak(commands.youtube_search(query))

    # ── Google Search ─────────────────────────────────────────────────────────
    elif "search" in command or "google" in command:
        query = command.replace("search", "").replace("google", "").strip()
        assistant.speak(commands.google_search(query))

    # ── Open Websites ─────────────────────────────────────────────────────────
    elif "open gmail" in command:
        assistant.speak(commands.open_website("gmail"))

    elif "open github" in command:
        assistant.speak(commands.open_website("github"))

    elif "open linkedin" in command:
        assistant.speak(commands.open_website("linkedin"))

    elif "open youtube" in command:
        assistant.speak(commands.open_website("youtube"))

    # ── Open Applications ─────────────────────────────────────────────────────
    elif "open chrome" in command:
        assistant.speak(commands.open_application("chrome"))

    elif "open vs code" in command or "open vscode" in command:
        assistant.speak(commands.open_application("vscode"))

    elif "open notepad" in command:
        assistant.speak(commands.open_application("notepad"))

    elif "open calculator" in command:
        assistant.speak(commands.open_application("calculator"))

    # ── Gemini — weather, jokes, and everything else ──────────────────────────
    else:
        assistant.speak(commands.ask_gemini(command))

    return True


def main():
    assistant.speak(f"Hello! I am {assistant.name}, your personal voice assistant. How can I help you?")

    while True:
        command = assistant.listen()
        if command:
            should_continue = route_command(command)
            if not should_continue:
                break


if __name__ == "__main__":
    main()
