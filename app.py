import speech_recognition as sr
import webbrowser
from os import path


# use the audio file as the audio source
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Try talking without eating')
        except sr.RequestError:
            print('Get better internet')
        return voice_data


def print_audiofile(audiofile):
    with sr.AudioFile(audiofile) as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Try talking without eating')
        except sr.RequestError:
            print('Get better internet')
        return voice_data


def respond(audio):
    if ('stupid fat hobbit' in audio):
        print('shut up Smeagol')
    if ('potatoes' in audio):
        print('Whats "taters", eh?')
    if ('search' in audio):
        search = record_audio('What shall we search for Preciousss?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Precious, I foundss this for you...')


respond(record_audio())
