import speech_recognition as sr

rec = sr.Recognizer()
audio = rec.listen(sr.Microphone())

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + rec.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))