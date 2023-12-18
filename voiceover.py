"""
import pyttsx3

voiceoverDir = "Voiceovers"

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    engine = pyttsx3.init()
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath
"""

from gtts import gTTS
import os

voiceoverDir = "/Users/msundgren/RedditStuff/Voiceovers"

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    
    tts = gTTS(text=text, lang='en')
    tts.save(filePath)
    
    return filePath
