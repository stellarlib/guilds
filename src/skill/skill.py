from .skill_method_id import SkillMethodID as s_id
from random import randint


class Skill(object):

    def __init__(self, hero, name, symbol, value):

        self.hero = hero
        self.name = name
        self.symbol = symbol
        self.value = value
        self.skill_methods = {}

    def call_skill_method(self, skill_method_id):
        return self.skill_methods[skill_method_id]()

    @staticmethod
    def random_weight(min_w, max_w):
        return randint(min_w, max_w) / 100.0
