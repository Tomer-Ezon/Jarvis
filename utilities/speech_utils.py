import pyttsx3

from brain.jarvis import Listener
from utilities.logger import Logger

logger = Logger()
voice = pyttsx3.init(debug=True)
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)


def say(data_to_say):  # work with pyaudop
    # voice.say(data_to_say)
    # voice.runAndWait()
    logger.debug('Jarvis', data_to_say)


listener = Listener()


def yes_or_no_choice():
    text = listener.get_cli_input()
    return 'yes' in text