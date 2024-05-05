import speech_recognition
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser

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

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google","")
        query = query.replace("kaaf","")
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        speak("This is what i found on google")
        
        try:
            pywhatkit.search(query)
            results = googleScrap.summary(query, sentences=2)
            speak(results)
        except:
            speak("No spekable output")

def youTube(query):
    if "youtube" in query:
        speak("This is what i found for your search")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:   
        speak("Searching on wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("jarvis","")
        query = query.replace("search wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)  
    