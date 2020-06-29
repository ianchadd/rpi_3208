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


class Constants(BaseConstants):
    name_in_url = 'feedback_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    instructions_feedback = models.LongStringField(
        label = '',
        blank = True
    )
    general_feedback = models.LongStringField(
        label = '',
        blank = True
    )
    instruction_clear = models.StringField(
        label = 'The instructions were clear.',
        choices = ['Completely Agree', 'Agree', 'Neither agree nor disagree', 'Disagree', 'Completely Disagree']
    )   
    earnings_clear = models.StringField(
        label = 'The instructions helped me understand how my earnings are calculated.',
        choices = ['Completely Agree', 'Agree', 'Neither agree nor disagree', 'Disagree', 'Completely Disagree']
    )
