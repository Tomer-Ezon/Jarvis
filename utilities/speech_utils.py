import pyttsx3
from utilities.logger import Logger

logger = Logger()
voice = pyttsx3.init(debug=True)
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)


def say(data_to_say):  # work with pyaudop
    voice.say(data_to_say)
    voice.runAndWait()
    logger.debug('Jack', data_to_say)
