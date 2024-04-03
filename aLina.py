import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hi Master  Good Morning!   Its been quite a while Hope Your night was spent well!")

    elif hour>=12 and hour<18:
        speak(" Hi Master Good Afternoon! How are you Its been a While  Waiting for your command")

    else:
        speak(" Hi Master Good Evening!")

    speak(" I am Alina  at your work master. ")
    speak("Is there anything that I can do for you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening to your command cheif")
        print("Listening to your command cheif")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognized the command cheif     Working on it")
        print("Recognized the command cheif Working on it ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Pardon cheif can you repeat your command")
        print("Pardon cheif can you repeat your command")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif "what's the market saying today" in query:
            webbrowser.open("https://www.moneycontrol.com/")
        elif 'check my Instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'play hindi songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=hindi+songs")
        elif 'play english songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=english+songs")
        elif 'play taylor swift songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=taylor+swift+songs")
        elif 'play selena gomez songs' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=selena+gomez+songs")
        elif 'play hindi movies' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=hindi+movies")
        elif 'open vaccine site' in query:
            webbrowser.open("https://www.cowin.gov.in/")
        elif 'open my mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?pli=1#inbox")
        elif 'open list of actors' in query:
            webbrowser.open("https://www.imdb.com/list/ls068010962/")
        elif  'open rich people list' in query:
            webbrowser.open("https://www.forbes.com/india-billionaires/list/")
        elif 'open shopping site' in query:
            webbrowser.open("https://www.amazon.in/")
        elif 'open my classroom for assignment'in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
        elif 'open todays market' in query:
            webbrowser.open("https://www.moneycontrol.com/")

        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me the time Alina' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'email to Aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ")
        # elif 'exit Alina' in query:
        #         speak("Exiting. Have a good day!")
        # exit()
       