import subprocess
import os

from brain.listener import Listener
from utilities.speech_utils import say

browsers = []


class Computer:
    def __init__(self):
        self.listener = Listener()
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

    def search_youtube(self):
        say('What would you like to search?')
        text = self.listener.get_cli_input()
        self.browser.search_youtube(text)


class Browser:
    def __init__(self, chrome_path=''):
        self.chrome_path = chrome_path
        self.youtube = Youtube(chrome_path)

    def open_chrome(self, url):
        subprocess.call([self.chrome_path, url])

    def search_youtube(self, data):
        self.youtube.search_youtube(data)


class Youtube:
    def __init__(self, chrome_path):
        self.chrome_path = chrome_path
        self.url = 'https://www.youtube.com/'
        self.youtube_search_url = 'https://www.youtube.com/results?search_query='

    def search_youtube(self, data):
        subprocess.call([self.chrome_path, f'{self.youtube_search_url}{data}'])
