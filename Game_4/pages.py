from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time, random


round_values = [0.25,0.50,0.75,1.00,1.25,1.50,1.75]

class Instructions(Page):
    def vars_for_template(self):
        round_values = ''
        for i in self.session.config['round_values']:
            round_values = round_values + '$' + i + ', '
        round_values = round_values[:len(round_values)-2]
        return {
            'participant_vars': self.participant.vars,
            'round_values': round_values,
            'piece_rate': self.session.config['piece_rate'],
        }

class Selection(Page):
    form_model = 'player'
    form_fields = ['attention_check', 'game_4_switch']
    def before_next_page(self):
        if (self.player.game_4_switch == Constants.round_values[0]):
            self.player.game_4_switch = '0'
        elif (self.player.game_4_switch == Constants.round_values[-1]):
            self.player.game_4_switch = str(float(Constants.round_values[-1]) + 0.001)
        self.participant.vars['game_4_switch'] = self.player.game_4_switch
    def vars_for_template(self):
        game_1_score = 0
        try: # try catch since apps are skipped in testing
            game_1_score = int(self.participant.vars['game_1_score'])
        except:
            pass
        return {
            'game_1_score': game_1_score,
            'participant_vars': self.participant.vars,
            'piece_rate': self.session.config['piece_rate']
        }


page_sequence = [Instructions, Selection]