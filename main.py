
import speech_recognition
import pyaudio

sr = speech_recognition.Recognizer()#начало роботы с библиотекой
sr.pause_threshold = 0.5#пауза между словами
with speech_recognition.Microphone() as micro:#закаментироват потом
    sr.adjust_for_ambient_noise(source=micro,duration=0.5)#настройка уровня шума
    audio = sr.listen(source= micro)
    kladovka = sr.recognize_google(audio_data= audio,language="ru-RU")
print(kladovka)


