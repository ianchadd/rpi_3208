from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    form_model = 'player'
    form_fields = []
    
class Age(Page):
    form_model = 'player'
    form_fields = ['age', 'yob']

class Sex(Page):
    form_model = 'player'
    form_fields = ['sex']

class Gender(Page):
    form_model = 'player'
    form_fields = ['male',
                   'female',
                   't_male',
                   't_female',
                   'gnc',
                   'other_g',
                   'diff_gend']
    
class Orientation(Page):
    form_model = 'player'
    form_fields = ['orientation',
                   'other_orientation']

class S_History(Page):
    form_model = 'player'
    form_fields = ['sex_hist',
                   'attracted_men',
                   'attracted_women']
    
class Relationship(Page):
    form_model = 'player'
    form_fields = ['relationship',
                   'other_relationship']

class Primary_Earner(Page):
    def is_displayed(self):
        return self.player.relationship != 'Single'
    
    form_model = 'player'
    form_fields = ['primary_earner']

class Income(Page):
    form_model = 'player'
    form_fields = ['income']

class Ethnicity(Page):
    form_model = 'player'
    form_fields = ['ethnicity',
                   'other_ethnicity']

class Religion(Page):
    form_model = 'player'
    form_fields = ['religion',
                   'other_religion']
    
class Politics(Page):
    form_model = 'player'
    form_fields = ['politics']

class Location(Page):
    form_model = 'player'
    form_fields = ['live_in',
                   'grew_up_in']


page_sequence = [Instructions,
                 Age,
                 Sex,
                 Gender,
                 Orientation,
                 S_History,
                 Relationship,
                 Primary_Earner,
                 Income,
                 Ethnicity,
                 Religion,
                 Politics,
                 Location]
