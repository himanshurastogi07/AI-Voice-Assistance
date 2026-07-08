import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        speak("Sorry, I did not understand.")
        return ""

speak("Hello, I am your desktop assistant.")

while True:
    command = take_command()

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening google")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        speak(result)

    elif "exit" in command:
        speak("Goodbye")
        break