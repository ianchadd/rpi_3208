from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Instructions(Page):
    def before_next_page(self):
        # user has 90 seconds to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + self.session.config["seconds_for_counting_task"]
    def vars_for_template(self):
        round_values = ''
        for i in self.session.config['round_values']:
            round_values = round_values + '$' + i + ', '
        round_values = round_values[:len(round_values)-2]
        return {
            'participant_vars': self.participant.vars,
            'piece_rate': int(100* self.session.config['piece_rate']),
            'time_limit': self.session.config['seconds_for_counting_task'],
            'round_values': round_values
        }


page_sequence = [Instructions]
