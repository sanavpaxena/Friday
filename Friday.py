import datetime
import os
import random
import smtplib
import time
import webbrowser
import PyPDF2
import pyttsx3
import speech_recognition as sr
import wikipedia
from email.message import EmailMessage

email_list = {
    'dad': 'hiren.saxena@gmail.com',
    'mom': 'raginisaxena7118@gmail.com',
    'me': 'panav3.saxena@gmail.com',
    'me1': 'panavsaxena.panav@gmail.com',
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good morning')
    elif hour >=12 and hour < 18:
        speak('Good aftrenoon')
    else:
        speak('Good evening')

    speak('Hi... I am Friday!.. how can i help you?')
def takeCommand(ask = False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        if ask:
            print(ask)
        audio = r.listen(source)
    try:
        print('Recogizing..')
        query = r.recognize_google(audio, language="en-in")
        print('User said:',query)
    except Exception:
        print('say that again please..')
        return "none"
    return query

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('your email id', 'Your password')
    email = EmailMessage()
    email['From'] = 'panav3.saxena@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def get_email_info():
    speak('To Whom you want to send email')
    name = takeCommand()
    receiver = email_list[name]
    print(receiver)
    speak('What is the subject of your email?')
    subject = takeCommand()
    speak('Tell me the text in your email')
    message = takeCommand()
    send_email(receiver, subject, message)
    speak('Hey lazy ass. Your email is sent')
    speak('Do you want to send more email?')
    send_more = takeCommand()
    if 'yes' in send_more:
        get_email_info()




if __name__ == '__main__':
    wishMe()
    time.sleep(1)
    while 1:
        query = takeCommand().lower()
        if "wikipedia" in query:
            try:
                # noinspection PyTypeChecker
                wiki = takeCommand("what do you want to search for?")
                url = 'https://google.com/search?q=' + wiki
                webbrowser.get().open(url)
                results = wikipedia.summary(wiki, sentences = 2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            except:
                speak("No results were found")
        elif "open youtube" in query:
            webbrowser.get().open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open gmail" in query:
            webbrowser.open("gmail.com")
        elif "play music" in query:
            music_dir = "E:\\MUSIC"
            songs = os.listdir(music_dir)
            print(songs)
            r = random.randint(0,9)
            os.startfile(os.path.join(music_dir, songs[r]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif "open code" in query:
            codePath = "C:\\Users\\panav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "open meet" in query:
            webbrowser.open("meet.google.com")
        elif "search" in query:
            # noinspection PyTypeChecker
            search = takeCommand('what do you want to search for?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('here is what i found for' + search)
        elif 'exit' in query:
            speak('Goodbye! have a good day')
            exit()
        # elif "youtube" in query:
        #     # noinspection PyTypeChecker
        #     search_term = takeCommand('What to search on Youtube?')
        #     url = f"https://www.youtube.com/results?search_query={search_term}"
        #     webbrowser.get().open(url)
        #     speak(f'Here is what I found for {search_term} on youtube')
        elif "location" in query:
            # noinspection PyTypeChecker
            location = takeCommand('What is the location?')
            url = f"https://google.nl/maps/place/" + location + "/&amp;"
            webbrowser.get().open(url)
            speak('here is the location' + location)
        elif "read" in query:
            book = open('python_tutorial.pdf','rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            for num in range(0,pages):
                page = pdfReader.getPage(num)
                text = page.extractText()
                speak(text)
        elif "thanks" in query:
            speak('Its my pleasure')
        elif 'what is your name' in query:
            speak("My name is FRIDAY.. I am your personal voice assistant.")

        elif "send email" in query:
            get_email_info()
