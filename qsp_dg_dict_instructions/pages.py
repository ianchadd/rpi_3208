from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = 'player'


    
class Recip_Choose_ID_O(Page):
    #player will be able to choose from a list of randomly generated ID options
    form_model = 'player'
    
    def vars_for_template(self):
        return dict(
            img='flag_survey/recip_id_choose.png',
            participant_vars = str(self.participant.vars)
        )

    def before_next_page(self):
        self.player.set_ID(self.player.chooseID)
        self.player.set_other_flag()

class Recip_Choose_Icon(Page):
    #player will choose a flag icon on this page
    form_model = 'player'
    def vars_for_template(self):
        return dict(
            img='flag_survey/recip_icon_choose.png',
            participant_vars = str(self.participant.vars)
        )

class Options_List(Page):
    form_model = 'player'
    def vars_for_template(self):
        my_list = []
        for i in self.participant.vars['recip_options']:
            my_list.append([i[0],'flag_survey/flags/flag_{}'.format(i[1])+'.png'])
        rows = 3
        return dict(
            recip_options = my_list,
            participant_vars = str(self.participant.vars)
        )

    

page_sequence = [
    #Informed_Consent,
    Instructions,
    #Choose_ID_R,
    #ID_result,
    #Choose_ID_C,
    Recip_Choose_ID_O,
    Recip_Choose_Icon,
    Options_List
]
