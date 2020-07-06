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

#sets full list of tick lengths; same for all subjects
tick_lengths = [100,200,300,400,500]

class Constants(BaseConstants):
    name_in_url = 'cw_practice'
    players_per_group = None
    num_rounds = 5
    


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            ticks = tick_lengths
            #randomize order of tick lengths at subject level
            random.shuffle(ticks)
            #store ticks to participant vars to persist across apps
            p.participant.vars['ticks'] = ticks
            #store points and barrier choices to participant vars to persist across apps
            p.participant.vars['points'] = []
            p.participant.vars['barriers'] = []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    barrier = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)

    
