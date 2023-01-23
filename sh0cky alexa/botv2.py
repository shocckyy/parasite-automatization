from logging.config import listen
from time import sleep
import pyttsx3
import speech_recognition as sr
import random
import requests
import os
import subprocess
from datetime import datetime
import time
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
now = datetime.now()

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Bocik: Nasłuchuje...")
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio, language='pl-PL')
                print(f":{query}")
                return query
                break
            except:
                print("Spróbuj ponownie")
while True:
    query = command().lower() ## takes user command 