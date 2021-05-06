
import data
import pyttsx3  # chuyển văn bản sang tiếng nói
from gtts import gTTS
import playsound
import datetime
import speech_recognition
import webbrowser

data.welcome()


def command():
  javis_ear = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as mic:
      # mic = speech_recognition.Microphone()
      print('Im listening')
      javis_listening = javis_ear.listen(mic)
  try:
      return javis_ear.recognize_google(javis_listening)
  except:
      return "I can't hear you, please speak again"

while True:
  input = command().lower()
  if "please speak again" in input:
    data.speak("I can't hear you, please speak again")

  if "google" in input:
    data.speak("what should I search sir?")
    search = command().lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    data.speak(f"here is your {search} on google")
  
  if "youtube" in input:
    data.speak("what should I search sir?")
    search = command().lower()
    url = f"https://www.youtube.com/results?search_query={search}"
    webbrowser.get().open(url)
    data.speak(f"here is your {search} on youtube")

  if "good bye" in input:
    data.speak("Good Bye Sir!")
    quit()
  else: 
    # data.speak("I'm listening")