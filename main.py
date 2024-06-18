import pyttsx3
import requests
import speech_recognition as sr
import keyboard
import os
import subprocess as sp

import webbrowser
import time
import pywhatkit as kit
from datetime import datetime
#from decouple import config
from random import choice
from utils import opening_text
from functions.online_ops import find_my_ip, search_on_google, search_on_wikipedia, play_on_youtube, send_email, get_latest_news, get_weather_report, get_random_joke, get_random_advice,send_whatsapp_message

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = 'Anshu'
HOSTNAME = 'JAARU'


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you? {USER}")


listening = False


def start_listening():
    global listening
    listening = True
    print("started listening ")


def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        #audio = r.listen(source, timeout=5)
        print("Recognizing....")
        queri = (r.recognize_google



                 (audio, language='en-in'))
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night sir,take care!")
            else:
                speak("Have a good day sir!")
            exit()

    except Exception as e:
        speak("Sorry I couldn't understand. Can you please repeat that?")
        queri = 'None'
    return queri


if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)

            elif "open notepad" in query:
                speak("Opening Notepad for you sir")
                notepad_path ="C:\\Windows\\notepad.exe"
                os.startfile(notepad_path)


            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(
                    f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

            elif "open youtube" in query:
                speak("What do you want to play on youtube sir?")
                video = take_command().lower()
                play_on_youtube(video)

            elif "open google" in query:
                speak(f"What do you want to search on google {USER}")
                query = take_command().lower()
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want to search on wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia,{results}")
                speak("I am printing in on terminal")
                print(results)


            elif "send an email" in query:
                speak("On what email address do you want to send sir?. Please enter in the terminal")
                receiver_add = input("Email address:")
                speak("What should be the subject sir?")
                subject = take_command().capitalize()
                speak("What is the message ?")
                message = take_command().capitalize()
                if send_email(receiver_add, subject, message):
                    speak("I have sent the email sir")
                    print("I have sent the email sir")
                else:
                    speak("something went wrong Please check the error log")



            elif "send whatsapp message" in query:
                speak('On what number should I send the message sir? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message sir?")
                message = take_command().lower()
                send_whatsapp_message(number, message)
                speak("I've sent the message sir.")

            elif "give me news" in query:
                speak(f"I am reading out the latest headline of today,sir")
                speak(get_latest_news())
                speak("I am printing it on screen sir")
                print(*get_latest_news(), sep='\n')

            elif 'joke' in query:
                speak(f"Hope you like this one sir")
                joke = get_random_joke()
                speak(joke)
                speak("For your convenience, I am printing it on the screen sir.")
                print(joke)

            elif "advice" in query:
                speak(f"Here's an advice for you, sir")
                advice = get_random_advice()
                speak(advice)
                speak("For your convenience, I am printing it on the screen sir.")
                print(advice)


            elif 'weather' in query:
                ip_address = find_my_ip()
                speak("tell me the name of your city")
                city = input("Enter name of your city")
                speak(f"Getting weather report for your city {city}")
                weather, temp, feels_like = get_weather_report(city)
                speak(f"The current temperature is {temp}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")



            








