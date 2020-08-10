import speech_recognition as sr
from os import path


# use the audio file as the audio source
r = sr.Recognizer()


def print_audiofile():
    with sr.AudioFile("./audio/speech.wav") as source:
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


respond(print_audiofile())
