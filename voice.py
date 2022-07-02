from gtts import gTTS
#pip install gtts

from playsound import playsound
#pip install playsound

audio = 'speech.mp3'

language = 'pt-br'

sp = gTTS(text='Mas grande é o Senhor na nossa vida',
lang=language, 
slow=False)

sp.save(audio)
playsound(audio)