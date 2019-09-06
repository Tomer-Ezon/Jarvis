import pyttsx3

from brain.jarvis import Listener
from utilities.logger import Logger
import speech_recognition as sr

logger = Logger()
voice = pyttsx3.init(debug=True)
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)


def say(data_to_say):  # work with pyaudop
    voice.say(data_to_say)
    voice.runAndWait()
    logger.debug('Jarvis', data_to_say)


listener = Listener()


def yes_or_no_choice():
    text = listener.listen_process()
    return 'yes' in text