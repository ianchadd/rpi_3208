from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class P_ID(Page):
    form_model = 'player'
    form_fields = ['p_ID']

    def _before_next_page(self):
        self.player.participant.vars['p_id_begin'] = self.player.p_ID


page_sequence = [P_ID]
