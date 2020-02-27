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


author = 'Gaby'

doc = """
simple pride flag survey
"""


class Constants(BaseConstants):
    name_in_url = 'introduction_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    randomID = models.StringField()
    customID = models.StringField()
    otherID = models.StringField()
    flag = models.IntegerField()
