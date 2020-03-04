from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = [
        #'randomID',
        #'customID',
        #'otherID',
        'my_flag']
    def vars_for_template(self):
        return dict(
            image_path_1='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][0]),
            image_path_2='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][1]),
            image_path_3='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][2]),
            image_path_4='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][3]),
            image_path_5='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][4]),
            image_path_6='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][5])
        )

    def before_next_page(self):
        self.player.set_flag()
        
class Choose_ID_R(Page):
    #player will click a button to choose a random ID on this page
    form_model = 'player'
    form_fields = ['show_ID']
    
    def before_next_page(self):
        self.player.set_random_id()
        self.player.set_ID(self.player.randomID)

    def vars_for_template(self):
        return dict(
            my_ID = self.player.participant.vars['randomID']
            )

class Choose_ID_C(Page):
    #player will be able to enter a custom string ID of 8 characters
    form_model = 'player'
    form_fields = ['customID']

    def before_next_page(self):
        self.player.set_ID(self.player.customID)
    
class Choose_ID_O(Page):
    #player will be able to choose from a list of randomly generated ID options
    form_model = 'player'
    form_fields = ['otherID']

    def before_next_page(self):
        self.player.set_ID(self.player.otherID)

class Choose_Flag(Page):
    #player will choose a flag icon on this page
    form_model = 'player'
    form_fields = ['my_flag']
    def vars_for_template(self):
        return dict(
            image_path_1='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][0]),
            image_path_2='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][1]),
            image_path_3='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][2]),
            image_path_4='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][3]),
            image_path_5='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][4]),
            image_path_6='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][5]),
            participant_vars = str(self.participant.vars)
        )

    def before_next_page(self):
        self.player.set_flag()
 
    

# #class ResultsWaitPage(WaitPage):
#     #def after_all_players_arrive(self):
#         pass


class Results(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.my_flag),
            my_ID = self.player.my_ID,
            participant_vars = str(self.participant.vars)
        )
    
class Eval_adj(Page):
    form_model = 'player'
    form_fields = [
        'adj_1',
        'adj_2',
        'adj_3',
        'adj_4',
        'adj_5',
        'adj_6',
        'adj_7',
        'adj_8',
        'adj_9',
        'adj_10']
        
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.my_flag),
            my_ID = self.player.my_ID,
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )


page_sequence = [
    #Choose_ID_R,
    #Choose_ID_C,
    Choose_ID_O,
    Choose_Flag,
    Results,
    Eval_adj
]
