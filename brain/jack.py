import json
import speech_recognition as sr
from os import path
from computer.computer import Computer
from utilities.logger import Logger
from utilities.speech_utils import say

logger = Logger()


class Jack:
    def __init__(self):
        self.pc = Computer()
        self.recognizer = sr.Recognizer()
        self.should_run = True
        with open(path.dirname(__file__) + '/knowledge.json') as f:
            self.knowledge = json.load(f)
        say('I am ready')

    def start(self):
        while self.should_run:
            self.serve()

    def serve(self):
        text = self.listen_process()
        if text:
            for known_task in self.knowledge['data']:
                if all(keyword.lower() in text.lower() for keyword in known_task['keywords']):
                    method_to_call = getattr(self.pc, known_task['todo']['func'])
                    say(known_task['say'])
                    method_to_call(*tuple(arg for arg in known_task['todo']['args']))
                    return
            say('Im sorry, but I dont know how to do that.')

    def stop(self):
        self.should_run = False
        say('shutting down')

    def listen_process(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source=source)
                    try:
                        text = self.recognizer.recognize_google(audio)
                        logger.debug('Input', text)
                        if 'jack shut down' in text.lower():
                            self.stop()
                            break
                        if 'jack' in text.lower():
                            return text.replace('jack', '')
                    except sr.UnknownValueError:
                        pass
            except OSError:
                pass





