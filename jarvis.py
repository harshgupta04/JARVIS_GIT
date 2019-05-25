import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib  #For this package we have to enable "less secured APPs permission other this can't be used"

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
      r.pause_threshold = 1
      audio = r.listen(source)

  try:
      print("Recognizing")
      query = r.recognize_google(audio,language='en-in')
      print(f"user said:,{query}\n")

  except Exception as e:
      #print(e)
      print("Say that again please...")
      return "none"
  return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo().starttls()
    server.login('youremaill@mgil.com','your-password')    # To use this funtionality we have enter a email id and its password
    server.sendmail('youremaill@mgil.com, to, content')
    server.close()
if __name__ == "__main__":
    wishme()
   # while True:
    if 1: 
        query = takeCommand().lower()   #for proper matching of query
        #logics for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wkikpedia...')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2) 
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'opne youtube' in query:
            webbrowser.open("youtube.com")
        elif 'opne youtube' in query:
            webbrowser.open("google.com")
        elif 'opne youtube' in query:
            webbrowser.open("stackoverflow.com")    
         
        elif 'play music' in query:
            music_dir = 'E:\\Music\\Rahul'   # We are using \\ to show '\' in string format
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now.strftime("%H:%H:%S")
            speak(f"Sir, the time is {strTime}")    
        elif 'open code' in query:
            codePath = "C:\\Users\\Rahul kakodiya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  
        elif  'email to harsh' in query    #To mail multiple ids we can use DICTIONARY where name can be used as keys and email ids as value
            try:
               speak("What should i say")   
               content = takeCommand() 
               to = "harshgupta0428@gmail.com"
               sendEmail(to, content)
               speak("Email has been sent!")
            expect Exception as e:
            print(e)
            speak("Error email can't be sent")
        


        if 'quit' in query:
            exit
