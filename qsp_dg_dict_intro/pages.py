from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class introduction(Page):
    form_model = 'player'

    def vars_for_template(self):
        par_vars = self.player.participant.vars
        task = par_vars['task']
        part = par_vars['part']
        return dict(
            par_vars = str(par_vars),
            task = task,
            part = part
            )

    def before_next_page(self):
        self.participant.vars['task'] += 1
        #self.participant.vars['part'] += 1



page_sequence = [
    introduction,
]
