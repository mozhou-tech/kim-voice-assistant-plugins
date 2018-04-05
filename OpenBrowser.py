# -*- coding: utf-8-*-
import logging, json
from src.plugins import is_all_word_segment_in_text, plugin_output
import requests, sys
from src.config import load_yaml_settings
import webbrowser

WORDS = ['打开浏览器', '百度搜索', '百度一下', '进入阿里云控制台', '我想看新闻']
PRIORITY = 1
logger = logging.getLogger()


def handle(text, mic, profile, iot_client=None,chatbot=None):
    if '百度' in text:
        search_text = ''.join(text)
        webbrowser.open('https://www.baidu.com/s?wd='+search_text)
        mic.say(search_text)
    elif is_all_word_segment_in_text(['阿里云'], text):
        webbrowser.open('https://home.console.aliyun.com/new')
        mic.say('阿里云控制台一打开')
    elif '新闻' in text:
        webbrowser.open('https://news.baidu.com')
    else:
        webbrowser.open('http://www.baidu.com')

def is_valid(text):
    return is_all_word_segment_in_text(WORDS, text)
