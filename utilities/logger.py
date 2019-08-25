from datetime import datetime


class Logger:
    def __init__(self):
        pass

    def debug(self, source, message):
        print(f'{datetime.now()} - {source} - {message}')