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
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        num_sample_participants = self.session.config['num_sample_participants']
        group_size = 3
        if self.round_number==1:
            for p in self.get_players():
                p.participant.vars['group'] = random.sample(range(0,10),k=group_size)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
