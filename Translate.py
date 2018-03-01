# -*- coding: utf-8-*-
import logging
from src.plugins import is_all_word_segment_in_text

WORDS = ["用英文怎么说", "翻译一下"]
PRIORITY = 0
logger = logging.getLogger()

def handle(text, mic, profile, iot_client=None,chatbot=None):
    mic.say('yifanyi')

def is_valid(text):

    return is_all_word_segment_in_text(WORDS, text)
