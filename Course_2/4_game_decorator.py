from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }


class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        super().__init__()
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    @abstractmethod
    def get_positive_effects(self):
        pass


class AbstractNegative(AbstractEffect):
    @abstractmethod
    def get_negative_effects(self):
        pass


class Berserk(AbstractPositive):

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Berserk"]

    def get_stats(self):
        stats_massive = self.base.get_stats()
        for key in stats_massive:
            if key in ["Agility", "Strength", "Endurance", "Luck"]:
                stats_massive[key] += 7
            elif key in ["Perception", "Charisma", "Intelligence"]:
                stats_massive[key] -= 3
        stats_massive["HP"] += 50
        return stats_massive


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]

    def get_stats(self):
        stats_massive = self.base.get_stats()
        for key in stats_massive:
            if key in ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]:
                stats_massive[key] += 2
        return stats_massive


class Weakness(AbstractNegative):

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]

    def get_stats(self):
        stats_massive = self.base.get_stats()
        for key in stats_massive:
            if key in ["Agility", "Strength", "Endurance"]:
                stats_massive[key] -= 4
        return stats_massive


class Curse(AbstractNegative):

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]

    def get_stats(self):
        stats_massive = self.base.get_stats()
        for key in stats_massive:
            if key in ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]:
                stats_massive[key] -= 2
        return stats_massive


class EvilEye(AbstractNegative):

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]

    def get_stats(self):
        stats_massive = self.base.get_stats()
        for key in stats_massive:
            if key == "Luck":
                stats_massive[key] -= 10
        return stats_massive
