from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            exchange_rate = self.participant.vars['points_per_dollar'],
            dp_img = 'no_choice/dp_example.png',
            participant_vars = str(str(self.participant.vars))
            )

class Instructions_NBO(Page):
    form_model = 'player'
    form_fields = []
    #need to add conditional logic to incorporate exo treatment
    def is_displayed(self):
        return self.round_number == 1 and (self.player.participant.vars['treat'] == 'nbo' or self.player.participant.vars['treat'] == 'exo')

    def vars_for_template(self):
        p = self.participant
        pvars = p.vars
        exo = pvars['treat'] == 'exo'
        return dict(
            participant_vars = str(pvars),
            exo = exo
            )
class Instructions_payment(Page):
    form_model = 'player'
    form_fields = []
    #need to add conditional logic to incorporate exo treatment
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        p = self.participant
        pvars = p.vars
        exo = pvars['treat'] == 'exo'
        return dict(
            nbo_scheme = pvars['treat'] == 'nbo',
            participant_vars = str(pvars),
            exo = exo
            )

class Instructions_options(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        nbo_scheme = self.participant.vars['treat'] == 'nbo' or self.participant.vars['treat'] == 'exo'
        if nbo_scheme:
            value_distribution_img = 'no_choice/distribution_nbo.png'
        else:
            value_distribution_img = 'no_choice/distribution.png'

        return dict(
            nbo_scheme = nbo_scheme,
            value_distribution_img = value_distribution_img,
            participant_vars = str(str(self.participant.vars))
            )

class Instructions_time(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return dict(
            participant_vars = str(str(self.participant.vars))
            )

class Instructions_option_example(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            opt_img = 'no_choice/option_images/option_example.png',
            participant_vars = str(str(self.participant.vars))
            )

class NBO_exo(Page):

    def is_displayed(self):
        self.player.exo_outside_option()
        if self.player.nbo_choice:
            self.player.set_value()
            self.player.set_payoff()
        return (self.participant.vars['treat'] == 'exo' and self.player.nbo_choice)

    def vars_for_template(self):
        return dict(
            participant_vars = str(str(self.participant.vars)),
            )

class NBO_choice(Page):
    form_model = 'player'
    form_fields = ['nbo_choice']

    def is_displayed(self):
        return self.participant.vars['treat'] == 'nbo'

    def vars_for_template(self):
        return dict(
            participant_vars = str(str(self.participant.vars)),
            )

    def before_next_page(self):
        if self.player.nbo_choice:
            self.player.set_value()
            self.player.set_payoff()

class Decision(Page):
    form_model = 'player'
    form_fields = ['option_choose']
    timeout_seconds = Constants.timeout

    def is_displayed(self):
        return self.player.nbo_choice == False or self.participant.vars['treat'] == 'baseline'
    def vars_for_template(self):
        self.player.set_option_values()
        self.player.set_round_max()
        vars_dict = {}
        img_list = []
        '''
        for i in range(Constants.num_options):
            vars_dict['img_'+str(i)] = 'no_choice/option_images/d_{}_o_'.format(self.participant.vars['order'][self.round_number-1])+str(i+1)+'.png'
        vars_dict['problem'] = self.participant.vars['order'][self.round_number-1]
        '''
        '''
        return dict(
            image_path_1='no_choice/option_images/d_{}_o_1.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_2='no_choice/option_images/d_{}_o_2.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_3='no_choice/option_images/d_{}_o_3.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_4='no_choice/option_images/d_{}_o_4.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_5='no_choice/option_images/d_{}_o_5.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_6='no_choice/option_images/d_{}_o_6.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_7='no_choice/option_images/d_{}_o_7.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_8='no_choice/option_images/d_{}_o_8.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_9='no_choice/option_images/d_{}_o_9.png'.format(self.participant.vars['order'][self.round_number-1]),
            image_path_10='no_choice/option_images/d_{}_o_10.png'.format(self.participant.vars['order'][self.round_number-1]),
            problem = self.participant.vars['order'][self.round_number-1]
        )
        '''
        for i in range(Constants.num_options):
            img_list.append([i+1,'no_choice/option_images/d_{}_o_'.format(self.participant.vars['order'][self.round_number-1])+str(i+1)+'.png'])

        return dict(
            img_list = img_list,
            problem = self.participant.vars['order'][self.round_number-1],
            option_values = self.player.option_values,
            round_max = self.player.round_max,
            exo = self.participant.vars['treat'] == 'exo'
            )

    def before_next_page(self):
            self.player.set_value()
            self.player.set_payoff()
            if self.timeout_happened:
                self.player.payoff = 0
            self.player.set_correct()

    def error_message(self,values):
        if type(values['option_choose']) == type(None):
            return 'You must select of the displayed options.'

class Results(Page):
    def vars_for_template(self):
        me = self.player
        return dict(
            my_decision=me.option_choose,
            my_value=me.value
        )

class Final_Results(Page):
    #exo conditional logic
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        return dict(
            my_payoff= self.player.in_round(self.player.participant.vars['pay_round']).payoff,
            my_pay_round = self.player.participant.vars['pay_round'],
            my_nbo_choice = self.player.in_round(self.player.participant.vars['pay_round']).nbo_choice,
            exo = self.participant.vars['treat'] == 'exo'
        )


page_sequence = [
    Instructions,
    Instructions_option_example,
    Instructions_NBO,
    Instructions_options,
    Instructions_time,
    Instructions_payment,
    NBO_exo,
    NBO_choice,
    Decision,
    #Results,
    Final_Results
]
