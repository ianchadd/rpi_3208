from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,

)
import random


author = 'Ian Chadd'

doc = """
Cash Widthdrawal Task adapted from Oprea (2014); cw.html adapted from survival.html sent by Ryan Oprea
"""

tick_lengths = [100,200]
class Constants(BaseConstants):
    name_in_url = 'cw'
    players_per_group = None
    num_rounds = 2
    


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            ticks = tick_lengths
            random.shuffle(ticks)
            p.participant.vars['ticks'] = ticks
            p.participant.vars['points'] = []
            p.participant.vars['barriers'] = []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    barrier = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)

    
