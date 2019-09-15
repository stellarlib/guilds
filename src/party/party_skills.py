from src.skill.skill_method_id import SkillMethodID as s_id
from random import randint


class Skills(object):

    def __init__(self, party):

        self.party = party
        self.members = self.party.members

        self._detect = {
            'treasure': self.detect_treasure,
            'artifact': self.detect_artifacts,
            'relic': self.detect_relics,
            'ore': self.detect_ore,
            'herb': self.detect_herbs,
            'trap': self.detect_trap,
            'scrap': self.detect_scrap,
            'game': self.detect_game
        }

    # core methods
    def sum_skill(self, skill, skill_method_id):

        skill_sum = 0.0

        for hero in self.members.active_roster:
            if hero.has_skill(skill):
                skill_sum += hero.get_skill(skill).call_skill_method(skill_method_id)

        return skill_sum

    def sum_skillset(self, skills, skill_method_id):

        return sum([self.sum_skill(skill, skill_method_id) for skill in skills])

    def has_skill(self, skills):

        for hero in self.members.active_roster:
            for skill in skills:
                if hero.has_skill(skill):
                    return True

        return False

    # specific methods
    def treasure_bonus(self):

        # triggered when claiming treasure item
        # returns float % of map.bonus_loot_pool to be awarded as silver

        return self.sum_skillset(['looter', 'scrounger', 'thievery', 'explorer', 'lock_picking'],
                                 s_id.BONUS_TREASURE)

    def artifact_bonus(self):

        return self.sum_skillset(['divination', 'scholar', 'arcane_lore'],
                                 s_id.BONUS_ARTIFACTS)

    def relic_bonus(self):
        return self.sum_skillset(['divination', 'scholar', 'sacred_lore'],
                                 s_id.BONUS_RELICS)

    def gather_herbs(self):

        herb_skills = ['natural_power', 'herb_lore', 'forager', 'hunter', 'survivalist']
        return self.has_skill(herb_skills)

    def healing_herbs(self):
        healing_herb_skills = ['natural_power', 'herb_lore']
        return self.has_skill(healing_herb_skills)

    def herb_bonus(self):

        return self.sum_skillset(['herb_lore', 'forager', 'hunter', 'survivalist', 'natural_power'],
                                 s_id.BONUS_HERB)

    def miner(self):
        return self.has_skill(['miner', 'delver'])

    def ore_bonus(self):

        return self.sum_skillset(['miner', 'delver', 'scrounger', 'illuminator'],
                                 s_id.BONUS_ORE)

    def game_bonus(self):

        return self.sum_skillset(['missile_weapon', 'marksman', 'hunter', 'trapper',
                                  'survivalist', 'stealth'],
                                 s_id.BONUS_GAME)

    def scrap_bonus(self):

        return self.sum_skillset(['scrounger', 'laborer'],
                                 s_id.BONUS_SCRAP)

    def supply_cost(self, map, cell):

        return

    def detect_cell(self, cell):

        if cell.empty or cell.contents == 'foe':
            return

        self._detect[cell.contents]()

    def detect_treasure(self):
        detect = self.sum_skillset(['thievery', 'looter', 'scrounger', 'illuminator',
                                    'divination', 'scouting'],
                                   s_id.DETECT_TREASURE)
        return detect < randint(0, 99)

    def detect_artifacts(self):
        detect = self.sum_skillset(['scholar', 'arcane_lore', 'illuminator', 'divination'],
                                   s_id.DETECT_ARTIFACTS)

        return detect < randint(0, 99)

    def detect_relics(self):
        detect = self.sum_skillset(['scholar', 'sacred_lore', 'illuminator', 'divination'],
                                   s_id.DETECT_ARTIFACTS)

        return detect < randint(0, 99)

    def detect_herbs(self):
        detect = self.sum_skillset(['scholar', 'herb_lore', 'illuminator', 'forager', 'hunter',
                                    'traveller', 'explorer', 'survialist', 'scouting'],
                                   s_id.DETECT_ARTIFACTS)

        return detect < randint(0, 99)

    def detect_ore(self):
        detect = self.sum_skillset(['delver', 'explorer', 'scrounger', 'illuminator', 'divination',
                                    'scouting', 'miner'],
                                   s_id.DETECT_ARTIFACTS)

        return detect < randint(0, 99)

    def detect_game(self):
        pass

    def detect_scrap(self):
        pass

    def detect_trap(self):
        detect = self.sum_skillset(['divination', 'illuminator', 'scouting', 'trapper',
                                    'theivery', 'hunter'],
                                   s_id.DETECT_ARTIFACTS)

        return detect < randint(0, 99)
