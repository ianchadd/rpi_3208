from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class introduction(Page):
    form_model = 'player'

    def vars_for_template(self):
        
        return dict(
            par_vars = str(self.player.participant.vars)
            )
        



page_sequence = [
    introduction,
]
