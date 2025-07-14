import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')


for voice in voices:
    if "Zira" in voice.name:
        engine.setProperty('voice', voice.id)
        break

engine.say("This is a woman's voice.")
engine.runAndWait()