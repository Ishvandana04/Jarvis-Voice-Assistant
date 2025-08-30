import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai

recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)
# engine.setProperty('volume', 1)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def aiProcess(command):
   
   # Gemini API key set karo
   genai.configure(api_key="AIzaSyBzu2RaFU7pQEslBGXFDGKTfllWkNIgK0k")

   # Text-to-Speech engine init
   engine = pyttsx3.init()
   engine.setProperty('rate', 170)  # Speech speed
   engine.setProperty('volume', 1)  # Volume level

   # Gemini model call
   model = genai.GenerativeModel("gemini-1.5-flash")
   response = model.generate_content(command)

   # Print aur speak output
   print(response.text)
   speak(response.text)
   

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")

   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")

   elif  "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")

   elif  "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")

   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      
      if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
      else:
            speak("Song not found in library")

   elif "news" in c.lower():

      newsapi = "pub_9ef0636eb2294b0abdb3a4fb957bb499"  # अपनी key यहां डालो
      url = f"https://newsdata.io/api/1/news?apikey={newsapi}&country=in&language=en"

      response = requests.get(url)
      if response.status_code == 200:
         data = response.json()
         articles = data.get("results", [])
         for article in articles:
            speak(article["title"])
            print(article["title"])

      else:
         print("Request failed:", response.status_code, response.text)

   else:
      # Let Open AI handle the requests
      Output = aiProcess(c)
      speak(Output)


 
                                                      
if __name__ == "__main__":
      speak("Initializing jarvis...")

      while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
       r = sr.Recognizer()
       
        
        # recognize speech using Google
       print("recognizing...")

       try:
            with sr.Microphone() as source:
              print("Listening!")
              audio = r.listen(source, timeout=2, phrase_time_limit=1)

              word= r.recognize_google(audio)
              print("Heard:", word)

            if "jarvis" in word.lower():
                speak("Ya")
                
        
                
                # Listen for command
                print("jarvis active...")
                with sr.Microphone() as source:
                 audio = r.listen(source)
                 command= r.recognize_google(audio)

                processCommand(command)
        
       except Exception as e:
            print("Error; {0}".format(e))

           
