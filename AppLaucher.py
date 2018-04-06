# -*- coding: utf-8-*-
import logging, json,os
from src.plugins import is_all_word_segment_in_text, plugin_output
import requests, sys
from src.config import load_yaml_settings
import webbrowser

WORDS = ['启动']
PRIORITY = 16
logger = logging.getLogger()


def handle(text, mic, profile, iot_client=None,chatbot=None):
    if '音乐' in text and '网易' in text:
        os.system('open /Volumes/MacintoshHD/AppHub/NeteaseMusic.app')
    elif '微信' in text:
        os.system('open /Volumes/MacintoshHD/AppHub/Wechat.app')
    elif 'word' in text:
        os.system('open /Volumes/MacintoshHD/AppHub/Microsoft\ Word.app')
    elif '终端' in text:
        os.system('open /Applications/Utilities/Terminal.app')

def is_valid(text):
    return is_all_word_segment_in_text(WORDS, text)
