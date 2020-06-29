from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Feedback(Page):
    form_model = 'player'
    form_fields = ['instructions_clear', 'general_feedback']



page_sequence = [Feedback]
