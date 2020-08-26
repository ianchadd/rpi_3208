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
    name_in_url = 'qsp_dg_recip_intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools
        treats = itertools.cycle(['id_first','id_second']) #id_first is ID selection > DG Instructions; id_second is the reverse
        
        for p in self.get_players():
            p.participant.vars['info_treat'] = next(treats) #sets treatment var at participant level with balanced treatment
            if 'info_treat' in self.session.config:
                p.participant.vars['info_treat'] = self.session.config['info_treat']

class Group(BaseGroup):
    pass



class Player(BasePlayer):
    pass

