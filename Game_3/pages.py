from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time, random


class Instructions(Page):
    def vars_for_template(self):
        round_values = ''
        for i in self.session.config['round_values']:
            round_values = round_values + '$' + i + ', '
        round_values = round_values[:len(round_values)-2]
        seed_data = self.session.config['seed_data']
        return {
            'participant_vars': self.participant.vars,
            'time_limit': self.session.config['seconds_for_counting_task'],
            'round_values': round_values,
            'piece_rate': int(100*self.session.config['piece_rate']),
            'seed_data': seed_data
        }
    pass

class Selection(Page):
    form_model = 'player'
    form_fields = ['attention_check', 'game_3_switch']
    def before_next_page(self):
        self.participant.vars['game_3_attn_check'] = self.player.attention_check,
        if (self.player.game_3_switch == Constants.round_values[0]):
            self.player.game_3_switch = '0'
        elif (self.player.game_3_switch == Constants.round_values[-1]):
            self.player.game_3_switch = str(float(Constants.round_values[-1]) + 0.001)
        self.participant.vars['game_3_switch'] = self.player.game_3_switch
        self.participant.vars['game_3_payment'] = random.choice(Constants.round_values)
        self.participant.vars['game_3_piece_rate'] = float(self.participant.vars['game_3_payment']) < float(self.participant.vars['game_3_switch'])
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'piece_rate': self.session.config['piece_rate']
        }

class Selection_Results(Page):
    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + self.session.config["seconds_for_counting_task"]
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars,
            'value': self.participant.vars['game_3_payment'],
            'game_3_piece_rate': self.participant.vars['game_3_piece_rate'],
            'piece_rate': self.session.config['piece_rate'],
            'time_limit': self.session.config['seconds_for_counting_task'],
        }


page_sequence = [Instructions, Selection, Selection_Results]
