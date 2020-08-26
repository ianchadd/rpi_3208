from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class CW(Page):
    form_model = 'player'
    form_fields = ['barrier',
                   'points']

    def vars_for_template(self):
        ticks = self.player.participant.vars['ticks'][self.round_number-1]
        return {
            'participant_vars': self.participant.vars,
            'ticks': ticks

        }
    def before_next_page(self):
        p = self.player
        p.participant.vars['points'].append(p.points)
        p.participant.vars['barriers'].append(p.barrier)



page_sequence = [CW]
