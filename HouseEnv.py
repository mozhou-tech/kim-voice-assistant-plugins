# -*- coding: utf-8-*-
import logging, json
from src.plugins import is_all_word_segment_in_text
import requests, sys
from src.config import load_yaml_settings
from src.components.homeassistant import Hass

WORDS = ["室内气温", "室内温度","室内湿度","房间湿度", "室内亮度"]
PRIORITY = 11
logger = logging.getLogger()


def handle(text, mic, profile, iot_client=None, chatbot=None):
    """
    室内环境获取，例如温度、湿度、光照强度等等
    :param text:
    :param mic:
    :param profile:
    :param iot_client:
    :param chatbot:
    :return:
    """
    hass = Hass.get_instance()
    hass.conn()
    if '温度' in text or '气温' in text:
        entity_id = load_yaml_settings()['hass']['entities']['sensor']['temperature']
        mic.say('室内气温，'+hass.get_entity_states(entity_id=entity_id)['state']+'摄氏度')
    elif '湿度' in text:
        entity_id = load_yaml_settings()['hass']['entities']['sensor']['humidity']
        mic.say('室内湿度，百分之' + hass.get_entity_states(entity_id=entity_id)['state'])
    elif '光线' in text or '亮度' in text:
        entity_id = load_yaml_settings()['hass']['entities']['sensor']['illumination']
        illumination = float(hass.get_entity_states(entity_id=entity_id)['state'])
        if illumination < 50:
            illumination_str = '光线较暗'
        elif 480 > illumination > 50:
            illumination_str = '光线温和'
        elif 800 > illumination > 480:
            illumination_str = '光线良好，适合阅读'
        elif illumination > 800:
            illumination_str = '光线较强'

        mic.say('室内光强，' + illumination_str)


def is_valid(text):
    return is_all_word_segment_in_text(WORDS, text)
