# -*- coding: utf-8-*-
import logging, json
from src.plugins import is_all_word_segment_in_text
import requests, sys
from src.config import load_yaml_settings
from src.components.homeassistant import Hass
from random import randint
from time import sleep
from threading import Thread

WORDS = ["打开夜灯", "关闭夜灯","夜灯蓝色","夜灯红色", "绿色夜灯", "夜灯状态", "夜灯调亮", "夜灯调暗","庆祝一下"]
HELP_TEXT = ''
PRIORITY = 11
logger = logging.getLogger()


def handle(text, mic, profile, iot_client=None, chatbot=None):
    entity_id = load_yaml_settings()['hass']['entities']['light']['gateway_light']
    hass = Hass.get_instance()
    hass.conn()
    hass_entity_state = hass.get_entity_states(entity_id=entity_id)
    if '打开' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', brightness=50)
        mic.say('ok 啦')
    elif '关闭' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_off', brightness=50)
        mic.say('ok 啦')
    elif '蓝色' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', rgb_color=(0, 0, 255),
                                  brightness=hass_entity_state['attributes']['brightness'])
        mic.say('ok 啦')
    elif '白色' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', rgb_color=(255, 255, 255),
                                  brightness=hass_entity_state['attributes']['brightness'])
        mic.say('ok 啦')
    elif '红色' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', rgb_color=(255, 0, 0),
                                  brightness=hass_entity_state['attributes']['brightness'])
        mic.say('ok 啦')

    elif '绿色' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', rgb_color=(0, 255, 0),
                                  brightness=hass_entity_state['attributes']['brightness'])
        mic.say('ok 啦')

    elif '调暗' in text:
        new_brightness = hass_entity_state['attributes']['brightness'] - 25
        hass.xiaomi_gateway_light(entity_id=entity_id,
                                  rgb_color=hass_entity_state['attributes']['rgb_color'],
                                  brightness=new_brightness)
        mic.say('ok 啦')
    elif '调亮' in text:
        new_brightness = hass_entity_state['attributes']['brightness'] + 25
        hass.xiaomi_gateway_light(entity_id=entity_id,
                                  rgb_color=hass_entity_state['attributes']['rgb_color'],
                                  brightness=new_brightness)
        mic.say('ok 啦')

    elif '状态' in text:
        print(hass_entity_state['attributes'])

        if hass_entity_state['state'] == 'on':
            mic.say('夜灯已开启')
        else:
            mic.say('夜灯已关闭'+hass_entity_state['attributes'])
    elif '庆祝' in text:
        def celebrate():
            i = 0
            while i < 100:
                hass.xiaomi_gateway_light(entity_id=entity_id,
                                          rgb_color=(randint(1, 255),randint(1, 255),randint(1, 255),),
                                          brightness=100)
                sleep(0.3)
                i = i + 1

        Thread(target=celebrate, daemon=True).start()
        mic.say('ok 啦')



def is_valid(text):
    return is_all_word_segment_in_text(WORDS, text)
