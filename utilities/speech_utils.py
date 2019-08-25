import pyttsx3
from utilities.logger import Logger

logger = Logger()
voice = pyttsx3.init()


def say(data_to_say):
    voice.say(data_to_say)
    voice.runAndWait()
    logger.debug('Jarvis', data_to_say)