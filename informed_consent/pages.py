from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Informed_Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def vars_for_template(self):
        return dict(
            informed_consent = self.session.config['consent']
            )
        



page_sequence = [
    Informed_Consent,
]
