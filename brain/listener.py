import speech_recognition as sr

from utilities.logger import Logger

logger = Logger()


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_process(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source=source)
                    try:
                        text = self.recognizer.recognize_google(audio)
                        logger.debug('Input', text)
                        if text:
                            return text
                    except sr.UnknownValueError:
                        pass
            except OSError:
                pass
