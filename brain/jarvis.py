import json
import speech_recognition as sr
from os import path
from computer.computer import Computer
from utilities.logger import Logger
from utilities.speech_utils import say

logger = Logger()


class Jarvis:
    def __init__(self):
        self.pc = Computer()
        self.recognizer = sr.Recognizer()
        self.should_run = True
        with open(path.dirname(__file__) + '/knowledge.json') as f:
            self.knowledge = json.load(f)

    def start(self):
        self.wait_for_start()
        while self.should_run:
            self.serve()

    def serve(self):
        self.wait_to_be_called()  # if shutting down here - will need another shut down - problem
        text = self.listen_process('')
        if text:
            for known_task in self.knowledge['data']:
                if all(keyword.lower() in text.lower() for keyword in known_task['keywords']):
                    method_to_call = getattr(self.pc, known_task['todo'])
                    say(known_task['say'])
                    method_to_call()

    def stop(self):
        self.should_run = False
        say('shutting down')

    def wait_for_start(self):
        self.wait_to_be_called()
        self.listen_process('Start')
        say('Sure')

    def wait_to_be_called(self):
        self.listen_process('Jarvis')
        say('Yes?')

    def listen_process(self, break_word):
        with sr.Microphone() as source:
            while True:
                audio = self.recognizer.listen(source=source)
                try:
                    text = self.recognizer.recognize_google(audio)
                    logger.debug('Input', text)
                    if 'jarvis shut down' in text.lower():
                        self.stop()
                        break
                    if break_word.lower() in text.lower():
                        return text
                except sr.UnknownValueError:
                    pass




