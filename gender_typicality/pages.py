from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = []

   # def set_formfields(self):
   #     self.form_fields.clear()
   #     self.form_fields.append(self.player.participant.vars['questions'][self.round_number - 1])
    
   # def is_displayed(self):
   #     if self.round_number <= self.participant.vars['num_questions']:
   #         self.set_formfields()
   #         return True
    
   # def vars_for_template(self):
   #     survey_title = self.session.config['survey_title']
   #     return dict(
   #         survey_title = survey_title,
   #         participant_vars = self.player.participant.vars
   #         )
   # def before_next_page(self):
   #     field = self.player.participant.vars['questions'][self.round_number - 1]
   #     self.participant.vars[field] = getattr(self.player, field)

class week(Page):
    form_model = 'player'
    form_fields = ['work_house',
                   'gymnastics',
                   'roller_blade',
                   'strenuous',
                   'walk',
                   'bike',
                   'talk',
                   'tv',
                   'hobby',
                   'sad',
                   'tired',
                   'video_games']


class year(Page):
    form_model = 'player'
    form_fields = ['damage',
                   'fight',
                   'substance']

class agreement(Page):
    form_model = 'player'
    form_fields = ['risks',
                   'imagination',
                   'dont_talk',
                   'stress',
                   'worry',
                   'mood',
                   'sympathize',
                   'others_interested',
                   'others_problems']

    
class general(Page):
    form_model = 'player'
    form_fields = ['weight',
                   'stretching',
                   'gun',
                   'sunblock',
                   'intelligent',
                   'pray',
                   'sun_hour',
                   'sweat']


class random(Page):
    form_model = 'player'
    form_fields = ['expelled',
                   'paid_sex',
                   'gambling',
                   'tobacco',
                   'arrested',
                   'military']



page_sequence = [week,
                 year,
                 agreement,
                 general,
                 random]
