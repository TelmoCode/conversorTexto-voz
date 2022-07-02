from tkinter import *

from gtts import gTTS
#pip install gtts

from playsound import playsound
#pip install playsound

audio = 'speech.mp3'

language = 'pt-br'

txt = 'Mas graças a Deus que nos dá vitória por Cristo Jesus nosso Senhor'

sp = gTTS(text=f"{txt}",
lang=language, 
slow=False)

sp.save(audio)
playsound(audio)

