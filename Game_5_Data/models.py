from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,

)
from custom_templates.custom_classes import DataPlayer


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Game_5_Data'
    players_per_group = None
    num_rounds = 1
    game_name = "game_5"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(DataPlayer):
    pass
