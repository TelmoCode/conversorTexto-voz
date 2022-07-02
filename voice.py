from gtts import gTTS

from playsound import playsound

audio = 'speech.mp3'

language = 'pt-br'

sp = gTTS(text='Mas grande é o Senhor na nossa vida',
lang=language, 
slow=False)

sp.save(audio)
playsound(audio)