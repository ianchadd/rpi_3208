from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random, json




class Summary(Page):
    def vars_for_template(self):
        payment_values = self.session.config['round_values']
        parvars = self.participant.vars
        if 'payment_game' in parvars:
            payment_game = parvars['payment_game']
        else:
            payment_game = random.randint(1,5)

        parvars['payment_game'] = payment_game
        parvars['game_1_value'] = [str(self.session.config['piece_rate'])]
        scheme = parvars['game_%d_scheme' % payment_game]
        score = parvars['game_%d_score' % payment_game]
        win = parvars['game_%d_place' % payment_game] == 1
        # check tiebreaker
        if parvars['game_%d_won_tiebreaker' % payment_game] not in (None, True):
            win = False
        # Calculate guess payment
        guess_payment = int(parvars['game_1_place'] == parvars['belief_game_1']) + int(parvars['game_2_place'] == parvars['belief_game_2'])
        #calc payout
        payment = parvars['game_%d_payout' % payment_game]
        payout = 1.5 + guess_payment + payment
        payment_value = None
        if payment_game is not 5:
            payment_value = parvars['game_%d_value' % payment_game]
        else:
            points_AB = json.loads(self.participant.vars['game_5_values'])
            print(points_AB)
            points_A = float(points_AB['Points_A'])/100
            points_B = float(points_AB['Points_B'])/100
            payment_value = 5 * points_B
        self.player.participant_vars = json.dumps(parvars)

        participation_fee = self.session.config['participation_fee']
        return {
            'payment_game': payment_game,
            'scheme': scheme,
            'score': score,
            'win': win,
            'guess_payment': guess_payment,
            'payment': payment,
            'payout': payout,
            'payment_value': payment_value,
            'participant_vars': parvars,
            'participation_fee': participation_fee
        }


page_sequence = [Summary]
