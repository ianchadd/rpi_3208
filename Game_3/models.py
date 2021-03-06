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


class Constants(BaseConstants):
    name_in_url = 'Game_3'
    players_per_group = None
    num_rounds = 1
    round_values = ["1.00"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attention_check = models.BooleanField(
        label = 'This question is to check your attention. Please select Option 1 below',
        choices = [
            [True, 'Option 1'],
            [False, 'Option 2']
            ],
        blank = True,
        )

    game_3_switch = models.StringField()
