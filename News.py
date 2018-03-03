# -*- coding: utf-8-*-
import logging, json
from src.plugins import is_all_word_segment_in_text, plugin_output
import requests, sys
from src.config import load_yaml_settings

WORDS = ['新闻', '今日头条']
PRIORITY = 12
logger = logging.getLogger()


def handle(text, mic, profile, iot_client=None,chatbot=None):
    host = 'http://toutiao-ali.juheapi.com'
    path = '/toutiao/index'
    method = 'GET'
    appcode = load_yaml_settings()['aliyun']['api_market']['appcode']
    querys = 'type=top'
    bodys = {}
    url = host + path + '?' + querys
    headers = {
        'Authorization': 'APPCODE ' + appcode,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    r = requests.request(method=method, url=url, data=bodys, headers=headers)
    data = json.loads(r.content.decode('utf8'))
    # print(data)
    if data['result']['stat'] == '1':
        print(data)
        news = []
        news_ding = []
        for item in data['result']['data']:
            # "来源" + item['author_name'] +
            news.append(item['title'])
            news_ding.append('['+item['title']+']('+item['url']+')    ')
        plugin_output(text, mic, '。\n'.join(news), True, ' | '.join(news_ding))
    else:
        mic.say('接口出错')



def is_valid(text):
    return is_all_word_segment_in_text(WORDS, text)
