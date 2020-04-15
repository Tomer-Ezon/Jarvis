import json

from os import path

from brain.listener import Listener
from computer.computer import Computer
from utilities.logger import Logger
from utilities.speech_utils import say

logger = Logger()


class Jarvis:
    def __init__(self):
        self.pc = Computer()
        self.listener = Listener()
        self.should_run = True
        self._refresh_knowledge()
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
            self.learn()

    def learn(self):
        say('Would you like me to learn?')
        answer = self.listen_process()
        if 'yes' in answer.lower():
            say('What are the keywords for this task? seperate them with a coma and space')
            keywords = self.listen_process().split(', ')
            say('What should I say?')
            what_to_say = self.listen_process()
            say('What func should I use?')
            func_name = self.listen_process()
            say('Arguments? insert them with coma and space')
            args = self.listen_process().split(', ')
            self._write_ability_to_file(keywords, func_name, args, what_to_say)

    def _write_ability_to_file(self, keywords, func_name, args, what_to_say):
        with open(path.dirname(__file__) + '/knowledge.json') as f:
            abilities = json.load(f)
        new_ability = {"keywords": keywords, "todo": {"func": func_name, "args": args}, "say": what_to_say}
        abilities['data'].append(new_ability)
        with open(path.dirname(__file__) + '/knowledge.json', 'w') as f:
            json.dump(abilities, f)
        self._refresh_knowledge()
        say('done')

    def _refresh_knowledge(self):
        with open(path.dirname(__file__) + '/knowledge.json') as f:
            self.knowledge = json.load(f)

    def stop(self):
        self.should_run = False
        say('shutting down')

    def listen_process(self):
        while True:
            text = self.listener.get_cli_input()
            if 'down' in text.lower() and 'jarvis' in text.lower() and 'shut' in text.lower():
                self.stop()
                break
            else:
                return text
