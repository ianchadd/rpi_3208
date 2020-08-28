from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    form_model = 'player'
    form_fields = []

    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )
class Birth(Page):
    form_model='player'
    form_fields = [
        'yob',
        'sex',
        ]

    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )
        
class Care(Page):
    form_model='player'
    form_fields = [
        'care_others',
        ]
    def is_displayed(self):
        return not self.session.config['recip']
    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )
class Gender_SO(Page):
    form_model='player'
    form_fields = ['male',
                   'female',
                   't_male',
                   't_female',
                   'gnc',
                   'nb',
                   'other_g',
                   'diff_gend',
                   'orientation',
                   'other_orientation'
                   ]
    
    def error_message(self,values):
        if values['male'] == 0 and values['female'] == 0 and values['t_male'] == 0 and values['t_female'] == 0 and values['gnc'] == 0 and values['nb'] == 0 and values['other_g'] == 0:
            return 'You must select at least one response.'
        elif values['other_g'] and type(values['diff_gend']) == type(None):
            return 'If you select Other, you must specify in the provided field'
        elif values['orientation'] =='Other (please state below)' and type(values['other_orientation']) == type(None) :
            return 'If you select Other, you must specify in the provided field'

    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )

class S_History(Page):
    form_model = 'player'
    form_fields = ['relations_same',
                   'relations_different',
                   'attraction_same',
                   'attraction_different',
                   'attn_check_4'
                   ]
    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )

class Gen_Demographics(Page):
    form_model = 'player'
    form_fields = [
                    'white',
                   'black',
                   'native',
                   'asian',
                   'pacif_island',
                   'latino',
                   'arab',
                   'other_eth',
                   'other_ethnicity',
                    'relationship',
                   'other_relationship',
                   'education',
                   'income',
                   'religion',
                   'other_religion',
                   'live_in',
                   'other_live_location',
                   'grew_up_in',
                   'other_grew_up_location'
                   ]
    
    def error_message(self,values):
        if values['relationship'] =='Other (please state below)' and type(values['other_relationship']) == type(None):
            return 'If you select Other, you must specify in the provided field'
        elif values['other_eth'] and type(values['other_ethnicity']) == type(None):
            return 'If you select Other, you must specify in the provided field'
        elif values['religion'] =='Some other religious affiliation (please specify below)' and type(values['other_religion']) == type(None):
            return 'If you select Other, you must specify in the provided field'
        elif (values['live_in'] =='Other (please state below)' and type(values['other_live_location']) == type(None)) or (values['grew_up_in'] =='Other (please state below)' and type(values['other_grew_up_location']) == type(None)) :
            return 'If you select Other, you must specify in the provided field'
    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )

class Politics(Page):
    form_model = 'player'
    form_fields = ['econ_politics',
                   'social_politics',
                   'election_2016']
    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )

class LGBT_Attitudes(Page):
    form_model = 'player'
    form_fields = ['lgbt_free',
                   'lgbt_business',
                   'lgbt_adopt',
                   'lgbt_marriage',
                   'lgbt_bathroom'
                   ]
    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )
class LGBT_Experience(Page):
    form_model = 'player'
    form_fields = ['lgbt_met',
                   'lgbt_friend',
                   'consider_lgbt_ally',
                   'program_lgbt_ally']
    def before_next_page(self):
        self.player.participant_vars_dump(self)
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )

class Prolific_Guess(Page):
    form_model = 'player'
    form_fields = ['prolific_female',
                   'prolific_lgbt',
                   'prolific_ally',
                   'prolific_liberal',
                   'prolific_equal',
                   'prolific_conservative',
                   ]
    def is_displayed(self):
        return self.session.config['recip']
    def error_message(self,values):
        if values['prolific_liberal'] + values['prolific_equal'] + values['prolific_conservative'] != 100:
            return 'Your answers to the final three questions on this page must add up to 100.'
    def before_next_page(self):
        self.player.participant_vars_dump(self)
        self.participant.vars['part'] += 1
    def vars_for_template(self):
        recip = self.session.config['recip']
        return dict(
            self.player.vars_for_template(),
            recip = recip,
        )
    

page_sequence = [Instructions,
                 Birth,
                 Gender_SO,
                 S_History,
                 Gen_Demographics,
                 Politics,
                 Care,
                 LGBT_Attitudes,
                 LGBT_Experience,
                 Prolific_Guess]
