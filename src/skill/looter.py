from .skill import Skill, s_id


class Looter(Skill):

    def __init__(self, hero, value):

        Skill.__init__(self, hero, 'looter', 1, value)

        self.skill_methods = {
            s_id.BONUS_TREASURE: self.bonus_loot
        }

    def bonus_loot(self):
        weight = self.random_weight(90, 100)
        return self.value * .1 * weight
