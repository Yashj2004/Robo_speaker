import pyttsx3
system=pyttsx3.init()
while True:
    text=input("enter what you want to say:\t")
    if text=="exit":
        break
    system.say(text)
    system.runAndWait()
