import subprocess

import os

from utilities.speech_utils import say


class Computer:
    def __init__(self):
        self.browser = Browser(chrome_path=self.find_file('C:\\', 'chrome.exe'))

    def find_file(self, root_folder, file_name):
        for root, _, files in os.walk(root_folder):
            for f in files:
                if f == file_name:
                    return os.path.join(root, f)

    def open_chrome(self, url=''):
        if not self.browser.chrome_path:
            say('could not find google chrome on your computer')
        else:
            self.browser.open_chrome(url)


class Browser:
    def __init__(self, chrome_path=''):
        self.chrome_path = chrome_path

    def open_chrome(self, url):
        subprocess.call([self.chrome_path, url])