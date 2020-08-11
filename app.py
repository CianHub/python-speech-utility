import speech_recognition as sr
import webbrowser
from os import path
import time
import playsound
import random
from gtts import gTTS
from time import ctime
import os

# use the audio file as the audio source
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            smeagol_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            smeagol_speak('Can you repeat that please?')
        except sr.RequestError:
            smeagol_speak('Get better internet')
        return voice_data


def print_audiofile(audiofile):
    with sr.AudioFile(audiofile) as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            smeagol_speak('Can you repeat that please?')
        except sr.RequestError:
            smeagol_speak('Get better internet')
        return voice_data


def smeagol_speak(audio):
    text_speech = gTTS(text=audio, lang='en')
    r = random.randint(1, 100000000)
    audio_file = "audio-" + str(r) + '.mp3'
    text_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio)
    os.remove(audio_file)


def respond(audio):
    print(audio)
    if ('sam' in audio):
        smeagol_speak('Sam? He is a stupid fat hobbit')
    if ('potatoes' in audio):
        smeagol_speak('Whats "taters", eh?')
    if ('frank' or 'franklin' in audio):
        smeagol_speak('Frank? Oh he is a good boy!')
    if ('search' in audio):
        search = record_audio('What shall we search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        smeagol_speak('Precious, I foundss this for you...')
    if ('find location' in audio):
        location = record_audio('Where shall we go?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        smeagol_speak(
            'Here is the location you asked for it is' + location)
    if ('exit' in audio):
        exit()


smeagol_speak('How can I help you?')
time.sleep(1)
voice_data = record_audio()
respond(voice_data)
