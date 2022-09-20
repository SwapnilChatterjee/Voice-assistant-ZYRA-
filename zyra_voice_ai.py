import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING , WISH YOU HAVE A GREAT DAY AHEAD!!")
    elif hour>=12 and  hour<18:
        speak("GODD AFTERNOON")
    else:
        speak("GOOD EVENING")
    speak("I AM Zyra, YOUR ORDER IS MY COMMAND, HOW MAY I HELP YOU")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in' )
        print(f"User Said: {query} \n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "NONE"
    return query
def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('swapnilchatterjee.work@gmail.com' , '************')
    server.sendmail('swapnilchatterjee.work@gmail.com', to, content)
    server.close()
    

if __name__  == "__main__":
    print("WELCOME TO ZYRA AI")
    print("TO STOP ME TELL Zyra Quit")
    print("Say 'Show commands' to show the commands of the Tasks I can do!!!")
    wishMe()
    query = "Start"
    while (query != "stop"):
        query = TakeCommand().lower()
    # LOGIC FOR EXECUTING TASKS
        if 'wikipedia' in query:
           speak('Searching in Wikipedia...Please wait')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
        elif 'show commands' in query:
            speak("THE COMMANDS OF THE TASKS I CAN DO ARE....")
            print("1. say <topic name> wikipedia ------> to search in wikipedia")
            print("2. say open <app/website name> ------> to open the app or websites")
            print("3. say send email ------> to send mail")
            print("4. say what is the time ------> to know the current time in 24 hrs format")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open udemy' in query:
            webbrowser.open("udemy.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'open quora' in query:
            webbrowser.open("quora.com")
        elif 'open tiktok' in query:
            webbrowser.open("tiktok.com")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        elif 'open hackerearth' in query:
            webbrowser.open("hackerearth.com")
        elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
        elif 'open codewars' in query:
            webbrowser.open("codewars.com")
        
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        elif "open vs code" in query:
            path = "C:\\Users\\onlys\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "open chrome" in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        elif 'send email' in query:
            try:
                speak("Enter the email id to which mail is to be sent")
                to = input("ENTER THE MAIL id: ")
                speak("What should I say in the mail")
                content = TakeCommand()
                sendMail(to,content)
                speak("EMAIL HAS BEEN SENT!!!!!")
            except Exception as e:
                print(e)
                speak("Sorry the email cannot be sent..Please try again")


                
