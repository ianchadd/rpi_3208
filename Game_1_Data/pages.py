
from ._builtin import Page, WaitPage
from .models import Constants
from custom_templates.custom_funcs import (
    get_game_stats
)
import json

class Data(Page):
    def is_displayed(self):
        game_name = Constants.game_name
        participants = self.session.config["sample_participants"]
        participants = participants[:self.session.config["num_sample_participants"] + 1]
        
        self.player.calc_stats(game_name, participants)

        potential_payouts = self.player.calc_potential_payouts([str(self.session.config['piece_rate'])])
        
        self.player.payout = potential_payouts[str(self.session.config['piece_rate'])]
        self.participant.vars['game_1_value'] = [str(self.session.config['piece_rate'])]
        self.player.scheme = 'Piece Rate'
        self.participant.vars[game_name + '_scheme'] = self.player.scheme
        self.player.dump_vars(game_name, self.participant.vars)
        
        if self.session.config['data_pages_enabled']:
            return True
        else:
            return False
    def vars_for_template(self):
        game_name = Constants.game_name

        participants = self.session.config["sample_participants"]
        participants = participants[:self.session.config["num_sample_participants"] + 1]
        
        self.player.calc_stats(game_name, participants)

        potential_payouts = self.player.calc_potential_payouts([str(self.session.config['piece_rate'])])
        
        self.player.payout = potential_payouts[str(self.session.config['piece_rate'])]
        self.participant.vars['game_1_value'] = [str(self.session.config['piece_rate'])]
        self.player.scheme = 'Piece Rate'
        self.participant.vars[game_name + '_scheme'] = self.player.scheme
        self.player.dump_vars(game_name, self.participant.vars)
        return {
            'data' : self.player.data()
            }



page_sequence = [Data]
