import pyttsx3
import datetime

ai_mouth = pyttsx3.init()


def speak(output):
    ai_mouth.say(output)
    ai_mouth.runAndWait()


def getTime():
    time = datetime.datetime.now().strftime("%I: %M: %p")
    print(time)
    speak("Now is:" + time)


def welcome():
    welcome = "welcome back sir! How can I help you?"
    print(welcome)
    speak(welcome)


tro_dong_tu = ["be",
               "do", "does", "did",
               "have",
               "can", "could", "may", "might",
               "will", "shall", "would",
               "must", "need", "ought", "dare", "used"]
dong_tu_to_be = ["am", "is", "are",
                 "be", "being", "been",
                 "will be",
                 "was", "were", ]
tu_de_hoi = ["what", "how far", "where", "when",
             "why", "how often", "how", "who", "whom", "whose"]
