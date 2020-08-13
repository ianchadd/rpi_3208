from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            participant_vars = str(self.participant.vars)
        )
    
class DG_Instructions(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            participant_vars = str(self.participant.vars)
        )




class Recip_Offer(Page):
    form_model = 'player'
    form_fields = ['gave','attn_check_color', 'attn_check_color_2']
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            participant_vars = str(self.participant.vars)
        )

    def before_next_page(self):
        self.player.set_payoffs()

class Check_Understanding(Page):
    form_model = 'player'
    form_fields = ['check_understanding']
    def vars_for_template(self):
        return dict(
            participant_vars = str(self.participant.vars)
        )
'''
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )
'''

class Results(Page):
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'        
        return dict(
            #my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            #my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(self.participant.vars)
        )



page_sequence = [Introduction,
                 DG_Instructions,
                 Recip_Offer,
                 Check_Understanding,
                 #ResultsWaitPage,
                 #Results
                 ]
