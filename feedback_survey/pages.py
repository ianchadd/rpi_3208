from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Feedback(Page):
    form_model = 'player'
    form_fields = ['instruction_clear', 'earnings_clear', 'instructions_feedback', 'general_feedback']
   


page_sequence = [Feedback]
