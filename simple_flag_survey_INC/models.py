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
Survey (part 1) flag project
"""


class Constants(BaseConstants):
    name_in_url = 'simple_survey_flag'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    randomID = models.StringField() #need to turn this into a randomly generated number
    customID = models.StringField(
        choices=[]
        label = 'Please create your user ID'
        widget = widgets.RadioSelect,
    )
    otherID = models.StringField(label = 'Please choose one of the following as your ID')
    flag = models.IntegerField(label = 'Please enter a number corresponding to the profile image of your choice', min = 1, max = 3)
