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


author = 'Ian Chadd'

doc = """
Initial set of instructions for cw ai project
"""


class Constants(BaseConstants):
    name_in_url = 'cw_instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools
        treats = itertools.cycle(['female','male','neutral'])
        
        for p in self.get_players():
            p.participant.vars['treat'] = next(treats) #sets treatment var at participant level with balanced treatment
            if 'treat' in self.session.config:
                p.participant.vars['treat'] = self.session.config['treat']
            

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
