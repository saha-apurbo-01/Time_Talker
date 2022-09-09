import speech_recognition as sr
import pyttsx3
import datetime

google = pyttsx3.init()
listener = sr.Recognizer()



google.say("how can i help you sir")
google.runAndWait()


try:
   with sr.Microphone() as source:
       print("listening...")
       print("must be said : Play")
       voice = listener.listen(source)
       command = listener.recognize_google(voice)
       print(command)

   if "time" in command:
     time = datetime.datetime.now().strftime("%I:%M %p")
     print(time)
     google.say("current time is " + time)
     google.runAndWait()

except:
    pass
