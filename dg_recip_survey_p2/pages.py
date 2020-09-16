from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            details = 'dg_recip/details.pdf',
            participant_vars = str(pvars),
            task = task,
            part = part
        )
    def before_next_page(self):
        if self.participant.vars['info_treat'] == 'id_second':
            self.participant.vars['part'] += 1

class Average_Guess(Page):
    form_model = 'player'
    form_fields = [
        'average_guess'
        ]
    def is_displayed(self):
        return self.round_number == 1 or self.round_number == 2
    def vars_for_template(self):
        if self.round_number == 1:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'
        round_1 = self.round_number == 1
        round_2 = not round_1
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            round_1 = round_1,
            round_2 = round_2,
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(pvars),
            task = task,
            part = part
            )
    def before_next_page(self):
        self.player.participant_vars_dump(self)
        if self.round_number > 1:
            self.participant.vars['part'] += 1
    
class Survey_Partner(Page):
    form_model = 'player'
    form_fields = [
        'inferred_gender',
        'inferred_age',
        'inferred_orientation',
        'inferred_ally',
        'inferred_politics',
        'gender_confidence',
        'age_confidence',
        'orientation_confidence',
        'politics_confidence',
        'ally_confidence'
        ]
    def is_displayed(self):
        return self.round_number == 2 or self.round_number == 3
    def vars_for_template(self):
        if self.round_number == 2:
            their_flag = 'other_flag'
            their_id = 'other_id'
        else:
            their_flag = 'third_flag'
            their_id = 'third_id'
        round_2 = self.round_number == 2
        round_3 = not round_2
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            round_2 = round_2,
            round_3 = round_3,
            their_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars[their_flag]),
            their_ID = self.player.participant.vars[their_id],
            participant_vars = str(pvars),
            task = task,
            part = part
            )
    def before_next_page(self):
        self.player.participant_vars_dump(self)
        if self.round_number > 2:
            self.participant.vars['part'] += 1
    
class Self_Explain(Page):
    form_model = 'player'
    form_fields = [
        'id_explain',
        'icon_explain',
        ]
    def is_displayed(self):
        return self.round_number == 3
    def vars_for_template(self):
        pvars = self.participant.vars
        task = pvars['task']
        part = pvars['part']
        return dict(
            my_flag = 'flag_survey/flags/flag_{}.png'.format(self.player.participant.vars['my_flag']),
            my_ID = self.player.participant.vars['my_ID'],
            participant_vars = str(pvars),
            task = task,
            part = part
            )
    def before_next_page(self):
        self.player.participant_vars_dump(self)
        if self.participant.vars['info_treat'] == 'id_first':
            self.participant.vars['part'] += 1
        else:
            self.participant.vars['task'] += 1
            self.participant.vars['part'] = 0


page_sequence = [Introduction,
                 Average_Guess,
                 Survey_Partner,
                 Self_Explain
                 ]
