from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class introduction(Page):
    form_model = 'player'

    def vars_for_template(self):
        
        return dict(
            par_vars = str(self.player.participant.vars)
            )

    def app_after_this_page(self, upcoming_apps):
        if self.participant.vars['info_treat'] == 'id_second':
            self.participant.vars['my_flag'] = 0
            self.participant.vars['my_ID'] = '{Your Chosen String}'
            return 'dg_recip_survey'
        
        



page_sequence = [
    introduction,
]
