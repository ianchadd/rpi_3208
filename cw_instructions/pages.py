from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from custom_templates.custom_funcs import get_box


class Intro(Page):
    def vars_for_template(self):
        delay = self.session.config['delay']
        treat = self.player.participant.vars['treat']
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee'],
            'delay': delay,
            'treat': treat
        }

class Instructions(Page):
    def vars_for_template(self):
        delay = self.session.config['delay']
        treat = self.player.participant.vars['treat']
        return {
            'participant_vars': self.participant.vars,
            'participation_fee': self.session.config['participation_fee'],
            'delay': delay,
            'treat': treat
        }



page_sequence = [
    Intro,
    Instructions]
