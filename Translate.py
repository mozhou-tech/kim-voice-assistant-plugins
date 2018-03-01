# -*- coding: utf-8-*-
import logging, json
from src.plugins import is_all_word_segment_in_text
import requests, sys
from src.config import load_yaml_settings

WORDS = ["用英文怎么说", "用英语怎么说", "翻译一下", "翻译"]
PRIORITY = 11
logger = logging.getLogger()


def handle(text, mic, profile, iot_client=None,chatbot=None):
    text = ''.join(text)
    text = text.replace('翻译一下', '', 1)
    text =text.replace('翻译', '', 1)
    text =text.replace('用英语怎么说', '', 1)
    text =text.replace('用英文怎么说', '', 1)
    host = 'http://jisuzxfy.market.alicloudapi.com'
    path = '/translate/translate'
    method = 'GET'
    appcode = load_yaml_settings()['aliyun']['api_market']['appcode']
    querys = 'from=zh-CN&text=' + text + '&to=en&type=google'
    bodys = {}
    url = host + path + '?' + querys
    headers = {
        'Authorization': 'APPCODE ' + appcode,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    r = requests.request(method=method, url=url, data=bodys, headers=headers)
    data = json.loads(r.content.decode('utf8'))
    if int(data['status']) == 0:
        mic.say(data['result']['result'])
    else:
        mic.say('阿里云接口调用出错，检查一下插件吧')


def is_valid(text):
    return is_all_word_segment_in_text(WORDS, text)
