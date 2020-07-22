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



class Constants(BaseConstants):
    name_in_url = 'dg_qsp_survey'
    players_per_group = None #pairs are made ex-post
    num_rounds = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #inferred demographic variables
    inferred_gender = models.StringField(
        label = '',
        choices = ['Male','Female','Trans/Intersex/Other'],
        )
    inferred_age = models.StringField(
        label = '',
        choices = ['Under 18','18 - 24','25 - 34', '35 - 44','45 - 54', '55 - 64','65 or Older'],
        )
    inferred_orientation = models.StringField(
        label = '',
        choices = ['Heterosexual or Straight', 'Non-heterosexual or Non-straight'],
        )
    inferred_politics = models.StringField(
        label = '',
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        )

    inferred_ally = models.StringField(
        label = '',
        choices = ['Yes', 'No'],
        )
    
    #confidence variables
    gender_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    age_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    orientation_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    ally_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )
    politics_confidence = models.IntegerField(
        label = '',
        choices = [
            [1, 'I chose randomly'],
            [2, 'A little confident'],
            [3, 'Fairly confident'],
            [4, 'Highly confident']
            ]
        )

    #explanation variables
    give_explain = models.LongStringField(
        label = '')
    different_explain = models.LongStringField(
        label = '')

    #own id explanation variables
    id_explain = models.LongStringField(
        label = '')
    icon_explain = models.LongStringField(
        label = '')

    #open ended response
    thoughts = models.LongStringField(
        label ='First of all, what do you think of the study today?')

