from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PW_Entry(Page):
    form_model = 'player'
    form_fields = ['pw']
        
    def error_message(self,values):
        if values['pw'] != self.session.config['pw']:
            return 'The password is not correct.'


page_sequence = [
    PW_Entry,
]
