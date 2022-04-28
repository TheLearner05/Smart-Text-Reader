from threading import Thread,Event,Timer
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

global r

class Speech2Text():
    def __init__(self):
        pass
    def speak(self,text):
        txt = "%s" % (text)
        tts = gTTS(text=txt)
        filename = 'speech.mp3'
        tts.save(filename)
        playsound(filename)

    def sp2txt(self):
        global r
        global audio
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("sayyyy")
            audio = r.listen(source,7,5)
            print(audio)
    def talk2pi(self):
        self.weltxt = "Hello. Welcome to this journey of learning with Smart Text Reader!! Please select the preferred language"
        self.speak(self.weltxt)
        self.sp2txt()
        try:
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            lang = r.recognize_google(audio)
            lang=lang.split(" ")[-1]

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
        return lang
    
    


    

   
    
   


