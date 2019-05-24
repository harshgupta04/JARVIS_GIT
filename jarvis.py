import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) 
engine.setProperty('voice',voices[0].id)



def speak(audio):
 engine.say(audio)
 engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak ("Good Morning!")

    elif hour>=12 and hour<18:
        speak ("Good Evening!")
    
    else:
        speak ("Good Evening!")
    speak("I am Jarvis Sir. How may I help you")

def takeCommand():
 # takes audio input and provides output in form of string
  r = sr.Recognizer()
  with sr.Microphone as source:
      print("Listening....")
      r.pause_threshold=1
      audio = r.listen(source)

  try:
      print("Recognizing")
      query = r.recognize_google(audio,language='en-in')
      print("user said:",query)

  except Exception as e:
      print(e)
      print("Say that again please...")
      return "none"
  return query


if __name__ == "__main__":
     wishme()
     takeCommand()

