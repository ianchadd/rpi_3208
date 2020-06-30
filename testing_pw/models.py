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
from django import forms
import random



author = 'Ian'


doc = """
Informed Consent App
"""


class Constants(BaseConstants):
    name_in_url = 'pw_entry'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass



class Player(BasePlayer):
    pw = models.StringField(
        label = '')


