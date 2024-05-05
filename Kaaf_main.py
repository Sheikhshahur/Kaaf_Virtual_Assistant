import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup


from GreetMe import greetMe



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4)
            print("Understanding ....")
            query = r.recognize_google(audio, language="en-in")
            print(f"You say : {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Can you repeat?")
        except sr.RequestError as e:
            print(f"Request error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        return None
    return

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Sir,You can Call me Anytime")
                    break
                
                elif "hello" in query:
                    speak("hello sir, how are you?")
                
                elif "i am fine" in query:
                    speak("that's great sir.")
                
                elif "how are you" in query:
                    speak("I am doing well sir, thank you for asking.")
                
                elif "thank you" in query:
                    speak("you are welcome, sir")
                    
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "temperature" in query:
                    search = "temperature in maharashtra"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                
                elif "weather" in query:
                    search = "temperature in maharashtra"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                
                
                    