from gtts import gTTS
import os

# Text to be converted to speech
text = (input("Enter the text : "))

# Initialize the gTTS object
tts = gTTS(text=text, lang='en')

# Save the audio file
tts.save("output.mp3")

# Play the saved audio file
os.system("output.mp3")
