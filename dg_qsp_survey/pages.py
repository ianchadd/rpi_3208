from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'
        task_2 = self.round_number == 1
        task_3 = not task_2
        return dict(
            task_2 = task_2,
            task_3 = task_3,
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(self.participant.vars)
        )

class Survey_Partner(Page):
    form_model = 'player'
    form_fields = [
        'inferred_gender',
        'inferred_age',
        'inferred_orientation',
        'inferred_politics',
        'gender_confidence',
        'age_confidence',
        'orientation_confidence',
        'politics_confidence'
        ]
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'
        task_2 = self.round_number == 1
        task_3 = not task_2
        return dict(
            task_2 = task_2,
            task_3 = task_3,
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(self.participant.vars)
        )
class Partner_Explain(Page):
    form_model = 'player'
    form_fields = [
        'give_explain'
        ]
    def is_displayed(self):
        return self.round_number == 2
    def vars_for_template(self):
        task_2 = self.round_number == 1
        task_3 = not task_2
        return dict(
            task_2 = task_2,
            task_3 = task_3,
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            flag_1 = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['other_flag']),
            id_1 = self.player.participant.vars['other_id'],
            flag_2 = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['third_flag']),
            id_2 = self.player.participant.vars['third_id'],
            participant_vars = str(self.participant.vars),
            gave_1 = self.participant.vars['gave_1'],
            gave_2 = self.participant.vars['gave_2'],
        )
    
class Self_Explain(Page):
    form_model = 'player'
    form_fields = [
        'id_explain',
        'icon_explain',
        ]
    def is_displayed(self):
        return self.round_number == 2
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'
        task_2 = self.round_number == 1
        task_3 = not task_2
        return dict(
            task_2 = task_2,
            task_3 = task_3,
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(self.participant.vars)
        )


page_sequence = [Introduction,
                 Survey_Partner,
                 Partner_Explain,
                 Self_Explain
                 ]