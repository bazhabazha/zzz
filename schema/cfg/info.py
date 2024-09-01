# -*- coding: utf-8 -*-
"""
@file:      info
@time:      2024/8/21 01:00
@author:    sMythicalBird
"""

from .zero_info import ZeroConfig
from .fight_info import FightConfig
from .load import load_config, get_fight_logic, load_tactics

zero_cfg = load_config("zero.yaml", ZeroConfig)
fight_cfg = load_config("fight.yaml", FightConfig)
fight_logic_all = get_fight_logic()
fight_zero = load_tactics(fight_cfg.zero_fight, fight_logic_all)

buff_list = [
    "以太",
    "冻结",
    "暴击",
    "引燃",
    "感电",
    "能量",
    "强袭",
    "支援",
    "决斗",
    "护盾",
    "协助",
    "通用",
    "闪避",
    "研究",
    "邦布",
    "空洞",
    "诡术",
    "契合",
]

char_list = [
    "青衣",
    "朱鸢",
    "艾莲",
    "莱卡恩",
    "猫又",
    "11号",
    "丽娜",
    "珂蕾妲",
    "格莉丝",
    "露西",
    "派派",
    "妮可",
    "比利",
    "本",
    "苍角",
    "安比",
    "可琳",
    "安东",
]
