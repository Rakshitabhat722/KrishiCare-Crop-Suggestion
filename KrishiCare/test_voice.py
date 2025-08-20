from gtts import gTTS
from playsound import playsound

text = "ನಮಸ್ಕಾರ ರಕ್ಷಿತಾ, ಕೃಷಿಕೇರ್ ಗೆ ಸುಸ್ವಾಗತ"
tts = gTTS(text=text, lang='kn')
tts.save("voice.mp3")
playsound("voice.mp3")
