from fucns import *
TRIGGER_WORDS = {
    "spotify": open_spotify,    
    "browser": open_spotify,
    "search" : search_in_chrome
}

# Main function
def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        print("Say a command!")
        result = recognize_speech_from_mic(recognizer, microphone)
        if result["transcription"]:
            print("You said: {}".format(result["transcription"]))
            words = result["transcription"].lower().split()
            for word in words:
                if word in TRIGGER_WORDS:
                    TRIGGER_WORDS[word]()
        if not result["success"]:
            print("I didn't catch that. What did you say?\n")
        if result["error"]:
            print("ERROR: {}".format(result["error"]))

        # Optionally, break the loop if a specific word is detected
        if result["transcription"] and "stop" in result["transcription"].lower():
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
