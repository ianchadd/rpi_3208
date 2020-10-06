from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""
#a new comment

class Constants(BaseConstants):
    name_in_url = 'Game_4'
    players_per_group = None
    num_rounds = 1
    round_values = ["1.00"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attention_check = models.BooleanField(
        label = 'This question is to check your attention. Please select Option 2 below',
        choices = [
            [False, 'Option 1'],
            [True, 'Option 2'],
            [False, 'Option 3'],
            [False, 'Option 4']
            ],
            blank=True
        )
    game_4_switch = models.StringField()
