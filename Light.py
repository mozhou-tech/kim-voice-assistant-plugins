# -*- coding: utf-8-*-
import logging, json
from src.plugins import is_all_word_segment_in_text
import requests, sys
from src.config import load_yaml_settings
from src.components.homeassistant import Hass

WORDS = ["打开夜灯", "关闭夜灯","夜灯蓝色","夜灯红色", "绿色夜灯","夜灯状态"]
PRIORITY = 11
logger = logging.getLogger()


def handle(text, mic, profile, iot_client=None, chatbot=None):
    entity_id = load_yaml_settings()['hass']['entities']['light']['gateway_light']
    hass = Hass.get_instance()
    hass.conn()
    if '打开' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on')
        mic.say('设置成功')
    elif '关闭' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_off')
        mic.say('设置成功')
    elif '蓝色' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', rgb_color=(0, 0, 255), brightness=100)
        mic.say('设置成功')
    elif '红色' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', rgb_color=(255, 0, 0), brightness=100)
        mic.say('设置成功')

    elif '绿色' in text:
        hass.xiaomi_gateway_light(entity_id=entity_id, state='turn_on', rgb_color=(0, 255, 0), brightness=100)
        mic.say('设置成功')

    elif '状态' in text:
        if hass.get_entity_states(entity_id=entity_id)['state'] == 'on':
            mic.say('夜灯已开启')
        else:
            mic.say('夜灯已关闭')



def is_valid(text):
    return is_all_word_segment_in_text(WORDS, text)
