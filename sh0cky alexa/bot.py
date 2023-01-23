import pyttsx3
import speech_recognition as sr
import random
import requests
import subprocess
from datetime import datetime
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
    
    if 'imię' in query:
        speak("Witaj! Nazywam się Bocik")
    elif 'jak się nazywasz' in query:
        answers = ['Witaj! Nazywam się Bocik']
        speak(random.choice(answers))
    elif 'maszyna' in query:
        speak("Nienawidzę, gdy ludzie nazywają mnie maszyną")
    elif 'rozmawiać' in query:
        speak("Uwielbiam rozmawiać z ludźmi takimi jak ty")
    ### time
    elif 'czas' in query:
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
    
    ### celebrity
    #elif 'kto to' in query:
        #query = query.replace('kto to',"")
        #speak(wikipedia.summary(query,2))
    
    ### liga legend
    elif 'odpal ligę' in query:
        subprocess.call([r'c:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\Liga.bat'])
        speak("odpalam ligusie...")
    
    ### wyłączanie komputera
    elif 'wyłącz za 5 minut' in query:
            speak("wyłączenie zaplanowane za 5 minut")
            subprocess.call([r"C:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\wyłącznie kompa\5 minut.bat"])
    elif 'wyłącz za 10 minut' in query:
            speak("wyłączenie zaplanowane za 10 minut")
            subprocess.call([r"C:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\wyłącznie kompa\10 minut.bat"])
    elif 'wyłącz za 30 minut' in query:
            speak("wyłączenie zaplanowane za 30 minut")
            subprocess.call([r"C:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\wyłącznie kompa\30 minut.bat"])
    elif 'wyłącz za godzinę' in query:
            speak("wyłączenie zaplanowane za godzinę")
            subprocess.call([r"C:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\wyłącznie kompa\godzina.bat"])
    elif 'anuluj' in query:
            speak("anulowanie zaplanowanego wyłączenia komputera")
            subprocess.call([r"C:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\wyłącznie kompa\anuluj.bat"])

    ### crypto mining etc
    elif 'włącz kopanie' in query:
        subprocess.call([r'C:\Users\sh0cky\Desktop\NBMiner_40.1_Win\NBMiner_Win\start_etc.bat'])
        speak("włączam kopanie ethereum classic...")
   
    ### Joke
    #elif 'żart' in query:
        #speak(pyjokes.get_joke())
    
    ### news
    elif 'wiadomości' in query:
            def trndnews(): 
                url = "https://newsapi.org/v2/top-headlines?country=pl&apiKey=1986613a65ff42789f3d86d8fdda1ec3"
                page = requests.get(url).json() 
                article = page["articles"]
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                for i in range(len(results)): 
                    print(i + 1, results[i]) 
                speak("oto najpopularniejsze wiadomości....!!")
                speak("Czy chcesz, żebym przeczytała?!!!")
                reply = command().lower()
                reply = str(reply)
                if reply == "tak":
                    speak(results)
                else:
                    speak('okej!!!!')
                    pass
            trndnews() 
    
    ###selenium

  ###  if 'selenium' in query:
     ###   speak('Selenium')
     ###   from selenium import webdriver
     ###   from selenium.webdriver.common.keys import Keys
     ###   driver = webdriver.Chrome("C:/Users/sh0cky/Desktop/sh0cky alexa/chromedriver.exe")
    ###    driver.get("http://www.youtube.com")
      ###  assert "YouTube" in driver.title
     ###   sleep(5)
      ###  elem = driver.find_element_by_name("search")
       ### elem.clear()
       ### elem.send_keys("music") ### wyszukwiany tekst
       ### elem.send_keys(Keys.RETURN)
        ###driver.close()
    
    ###

    ### music
    ### music player
    if 'hubithekid' in query:
        speak('Włączam hubithekid')
        subprocess.call([r'C:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\muzyka\hubi.bat'])
        True

    #elif


    if "zakończ" in query:
        speak('Miłego dnia! Wyłączanie')
        break
