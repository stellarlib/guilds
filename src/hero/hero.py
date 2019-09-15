from src.skill.skill_id import skill_ids


class Hero(object):

    def __init__(self):

        self.active = True
        self.skills = {}

    def has_skill(self, skill):
        assert skill in skill_ids
        return skill in self.skills

    def get_skill(self, skill):
        return self.skills.get(skill)
