from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class introduction(Page):
    form_model = 'player'

    def vars_for_template(self):
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        id_first = pvars['info_treat'] == 'id_first'
        self.player.info_treat = pvars['info_treat']
        return dict(
            par_vars = str(pvars),
            task = task,
            part = part,
            id_first = id_first
            )
    def before_next_page(self):
        self.participant.vars['task'] += 1

    def app_after_this_page(self, upcoming_apps):
        if self.participant.vars['info_treat'] == 'id_second':
            self.participant.vars['my_flag'] = 0
            self.participant.vars['my_ID'] = 'abcde123'
            return 'dg_recip_survey'





page_sequence = [
    introduction,
]
