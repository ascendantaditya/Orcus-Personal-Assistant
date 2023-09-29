import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am Jarvis sir. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Sun Rahe Hain...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Soch Rahe Hain...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Dubara Kuch Bolo...")
        return "None"
    return query

def sendEmail(to, content):
    
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('thegokueffect01@gmail.com', '@ditya2005A')
    server.sendmail('adityaacodes01@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    speak("Now the future will be changed ")
    wishme()
    #while True:
    if 1:
        query= takeCommand().lower()

   # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif ' open gmail' in query:
            speak("Opening Gmail")
            webbrowser.open("gmail.com")
        elif ' open github' in query:
            speak("Opening Github")
            webbrowser.open("github.com")
        
        elif 'email to modi' in query:
            try:
                speak("TRY KARTA HU BABA")
                content= takeCommand()
                to= "thegokueffect01@gmail.com"
                sendEmail(to, content)
                speak("Email bhej diya re baba!")
            except Exception as e:
                print(e)
                speak("Sorry baba, email nahi bhej paya")
            

        elif 'quit' in query:
            exit()

    
    