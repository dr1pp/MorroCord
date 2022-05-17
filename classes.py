from dataclasses import dataclass
from discord import Emoji

@dataclass
class Race:
    name: str


@dataclass
class Attribute:
    name: str
    emoji: str = Emoji



@dataclass
class Skill:
    id: int
    name: str
    attribute: Attribute


@dataclass
class PlayerClass:
    name: str

PLAYER_RACES = [
    Race("Argonian"),
    Race("Breton"),
    Race("Dark Elf"),
    Race("High Elf"),
    Race("Imperial"),
    Race("Khajiit"),
    Race("Nord"),
    Race("Orc"),
    Race("Redguard"),
    Race("Wood Elf")
]

PLAYER_ATTRIBUTES = [
    Attribute("Strength", "<:attributeStrength:976038388178243635>"),
    Attribute("Intelligence", "<:attributeIntelligence:976038387993694219>"),
    Attribute("Willpower", "<:attributeWillpower:976038387830120462>"),
    Attribute("Agility", "<:attributeAgility:976038387981103144>"),
    Attribute("Speed", "<:attributeSpeed:976038388052398100>"),
    Attribute("Endurance", "<:attributeEndurance:976038387964334100>"),
    Attribute("Personality", "<:attributePersonality:976038388144668672>"),
    Attribute("Luck", "<:attributeLuck:976038388090150932>")
]

PLAYER_SKILLS = [
    Skill(0, "Block", None),
    Skill(1, "Armorer", None),
    Skill(2, "Medium Armor", None),
    Skill(3, "Heavy Armor", None),
    Skill(4, "Blunt Weapon", None),
    Skill(5, "Long Blade", None),
    Skill(6, "Axe", None),
    Skill(7, "Spear", None),
    Skill(8, "Athletics", None),
    Skill(9, "Enchant", None),
    Skill(10, "Destruction", None),
    Skill(11, "Alteration", None),
    Skill(12, "Illusion", None),
    Skill(13, "Conjuration", None),
    Skill(14, "Mysticism", None),
    Skill(15, "Restoration", None),
    Skill(16, "Alchemy", None),
    Skill(17, "Unarmored", None),
    Skill(18, "Security", None),
    Skill(19, "Sneak", None),
    Skill(20, "Acrobatics", None),
    Skill(21, "Light Armor", None),
    Skill(22, "Short Blade", None),
    Skill(23, "Marksman", None),
    Skill(24, "Mercantile", None),
    Skill(25, "Speechcraft", None),
    Skill(26, "Hand-to-hand", None),


]

# Character picks 2 attributes, 1 specialization
# Player puts points into attributes on level up