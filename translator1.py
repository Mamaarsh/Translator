import speech_recognition as sp_r
import pyttsx3
from deep_translator import GoogleTranslator

class Translator:
    def __init__(self):
        self.word = ""

    def record_sound_to_word(self):
        rec = sp_r.Recognizer()
        with sp_r.Microphone() as source:
            print("Listening...")
            finaudio = rec.listen(source)
        try:
            self.word = rec.recognize_google(finaudio, language='en-US')
            if self.word.lower() == "shut down":
                print("Shutting down...")
                return False
            print("Your sentence is: " + self.word)
            return True
        except sp_r.UnknownValueError:
            print("Cannot understand your words!")
            return True
        except sp_r.RequestError as e:
            print(f"There is a problem with the system audio service (please try again): {e}")
            return True

    def play_sound(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 0.6)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    def translate(self):
        translated_word = GoogleTranslator(source='en', target='fa').translate(self.word)
        print("Translated sentence is: " + translated_word)
        return translated_word

while True:
    translator = Translator()
    print("Wellcome\n")
    if not translator.record_sound_to_word():
        break
    translator.play_sound(translator.word)
    translator.translate()
    print("____________________________")