import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
# import wolframalpha as wa
# import subprocess
# import os
# import json
# import requests


def speak(audio):
    engine = tts.init()

    # To change the voice of the AI, use the getProperty() method
    # And setProperty() method to set the voice to either male or female
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)

    engine.say(audio)
    engine.runAndWait()


def take_command():  # This method is for taking and recognizing commands

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Maverick is listening')

        # Seconds of non-speaking audio before a complete sentence
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print('Recognizing...')

            command = r.recognize_google(audio)
        except Exception as e:
            print(e)
            # speak('Kindly repeat your last command')
            return 'Repeat last command'
        return command


def tell_day():  # This function is for telling the day of the week

    day = datetime.datetime.today().weekday() + 1

    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in day_dict.keys():
        current_day = day_dict[day]
        speak('Today is {}'.format(current_day))


def tell_time():  # This function is for telling the time

    time = datetime.datetime.now().strftime('%H:%M')
    speak('The time is {}'.format(time) + ' hours')


def tell_date():  # This function is for telling the date.

    date = datetime.datetime.today().strftime("%d %B, %Y")
    speak('Today\'s date is {}'.format(date))


def hello():  # This function is for when Maverick is called upon

    speak('Hi, I am Maverick, your personal digital assistant. I am glad to be of assistance to you today.')


def take_query():  # This is function is for taking queries.

    hello()

    while True:
        query = take_command().lower()
        if "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif 'hi maverick' in query:
            speak('hello, what can i help you with')
            continue
        elif 'check wikipedia for' in query:
            speak('checking wikipedia')
            query = query.replace('check wikipedia for', '')

            result = wikipedia.summary(query, 3)
            # speak('According to Wikipedia,')
            speak('According to Wikipedia, ' + result)
            continue
        elif 'time' in query:
            tell_time()
            continue
        elif 'what is today' in query:
            tell_day()
            continue
        elif 'tell me the date' in query:
            tell_date()
            continue
        elif 'introduce yourself' in query:
            speak('My name is Maverick and I am a virtual digital assistant. I was created by Augustine to make'
                  'his life a breeze. I am still in development so I do not know so much about myself. Bear with me.')
            continue
        elif 'open my email' in query:
            speak('Opening email')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            continue
        elif 'can you tell me a joke' in query:
            speak('Of course, but my jokes are not funny.')
            speak(pyjokes.get_joke())
            continue
        elif 'on youtube' in query:
            video = query.replace('on youtube', '')
            speak('playing ' + video)
            pywhatkit.playonyt(video)
            continue
        elif 'thanks maverick' in query:
            speak('You\'re welcome boss.')
            continue
        elif 'what is your name' in query:
            speak('My name is Maverick, and I am a personal digital assistant.')
        else:
            pass


if __name__ == '__main__':
    take_query()
