from cgitb import text
from email.mime import audio
import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound

r=sr.Recognizer()
translator=google_translator()

with sr.Microphone()as source:
    print("speak now!")
    audio=r.listen(source)

    try:
        speech_text=r.recognize_google(audio)
        print(speech_text)

    except sr.UnknownValueError:
        print('could not understand')
    except sr.RequestError:
        print("could not request result from google")


    tranlated_text=translator.translate(speech_text) #lang_tgt='fr'
    print(tranlated_text)

    voice=gTTS (tranlated_text)
    voice.save("voice.mp3")
    playsound("voice.mp3")