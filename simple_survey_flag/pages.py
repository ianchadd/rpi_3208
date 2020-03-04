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
    form_fields = ['randomID']

class Choose_ID_C(Page):
    #player will be able to enter a custom string ID of 8 characters
    form_model = 'player'
    form_fields = ['customID']

class Choose_ID_O(Page):
    #player will be able to choose from a list of randomly generated ID options
    form_model = 'player'
    form_fields = ['otherID']

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
            image_path_6='flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag_choices'][5])
        )

    def before_next_page(self):
        self.player.set_flag()
 
    

# #class ResultsWaitPage(WaitPage):
#     #def after_all_players_arrive(self):
#         pass


class Results(Page):
    pass


page_sequence = [
    Choose_Flag
]
