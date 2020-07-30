from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = []
    
    def is_displayed(self):
        self.form_fields.append(self.player.participant.vars['questions'][self.round_number - 1])
        return self.round_number <= self.participant.vars['num_questions']
    
    def vars_for_template(self):
        survey_title = self.session.config['survey_title']
        return dict(
            survey_title = survey_title
            )


page_sequence = [Question]
