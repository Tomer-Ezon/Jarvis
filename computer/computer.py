import subprocess
import os

import time

from brain.listener import Listener
from utilities.speech_utils import say, yes_or_no_choice
from selenium import webdriver

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
        say('What would you like to search - you should say ONLY what you want to search!')
        text = self.listener.listen_process()
        self.browser.search_youtube(text)


class Browser:
    def __init__(self, chrome_path=''):
        self.chrome_path = chrome_path
        self.youtube = Youtube()

    def open_chrome(self, url):
        subprocess.call([self.chrome_path, url])

    def search_youtube(self, data):
        browser_instance = self.youtube.search_youtube(data)
        time.sleep(2)
        titles = browser_instance.find_elements_by_id(self.youtube.video_titles_id)
        for i in range(5):
            video_name = titles[i].text
            say(f'Would you like to watch the video {video_name}?')
            if yes_or_no_choice():
                titles[i].click()
                break
            if i == 4:
                say('Well, Look what you want to watch than.')


class Youtube:
    def __init__(self):
        self.url = 'https://www.youtube.com/'
        self.search_bar_id = 'search'
        self.search_bt_id = 'search-icon-legacy'
        self.video_titles_id = 'video-title'

    def search_youtube(self, data):
        browser = webdriver.Chrome('C:\\Users\\Tomer\\PycharmProjects\\Jarvis\\computer\\chromedriver.exe')
        browser.maximize_window()
        browser.get(self.url)
        self._search_content(data, browser)
        return browser

    def _search_content(self, content, browser):
        search_bar = browser.find_element_by_id(self.search_bar_id)
        search_bar.send_keys(content)
        browser.find_element_by_id(self.search_bt_id).click()
        time.sleep(1)


