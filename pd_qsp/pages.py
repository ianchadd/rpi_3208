from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )
    
class Scenario_1(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )
class Scenario_2(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )

class Scenario_3(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )

class Scenario_4(Page):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )

class Understanding(Page):
    form_model = 'player'
    form_fields = []
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )
    
class Decision_First(Page):
    form_model = 'player'
    form_fields = ['decision_first']
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )
    
class Decision_Second(Page):
    form_model = 'player'
    form_fields = ['decision_second']
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['third_flag']),
            their_ID = self.player.participant.vars['third_id'],
            participant_vars = str(self.participant.vars)
        )

class ResultsWaitPage(WaitPage):
    def vars_for_template(self):
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )

class Results_First(Page):
    def vars_for_template(self):
        return dict(
            my_decision = self.player.decision_first,
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            their_ID = self.player.participant.vars['other_id'],
            participant_vars = str(self.participant.vars)
        )

page_sequence = [Introduction,
                 Scenario_1,
                 Scenario_2,
                 Scenario_3,
                 Scenario_4,
                 Decision_First,
                 #ResultsWaitPage,
                 Results_First
                 ]
