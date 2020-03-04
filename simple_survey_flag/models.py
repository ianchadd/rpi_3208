from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from django import forms
import random


author = 'Gaby'
coauthor = 'Ian'


doc = """
Survey (part 1) flag project
"""


class Constants(BaseConstants):
    name_in_url = 'simple_survey_flag'
    own_ID = 'simple_survey_flag/own_ID.html'
    other_ID = 'simple_survey_flag/other_ID.html'
    players_per_group = None
    num_rounds = 1
    num_flags = 50 #number of flags in _static file other than pride flag
    num_choices = 5 #number of flags a player can choose from other than pride flag
    flag_choices = [] # list of all flag choices
    for i in range(num_flags):
        flag_choices.append(i+1)

choices2= ["HQQkF10d","pcrnTLUr","7OKdu5sV","wZPeexoH","UkTbcudD","zOz9aTis","9MEcfOL3","SVwZaZ7E""fFeJ8qw2","cRN5swzs","ePrKx7Ma","a1myqS0O","b4RWtHe9","F8I03MH2","C8feS7p2","K4zdqslW","3IbkRtps","CiBI3ZYx","9ME9zgnn","ZdIpJIRH"]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['my_flag_choices'] = Constants.flag_choices.copy()
            random.shuffle(p.participant.vars['my_flag_choices'])
            p.participant.vars['my_flag_choices'] = p.participant.vars['my_flag_choices'][:Constants.num_choices]
            p.participant.vars['my_flag_choices'].append(Constants.num_flags + 1)
            random.shuffle(p.participant.vars['my_flag_choices'])
            p.participant.vars['randomID'] = random.choice(choices2)
            p.participant.vars['treat_assign'] = random.random()
            if p.participant.vars['treat_assign'] <= 0.5:
                p.participant.vars['other_flag'] = Constants.num_flags + 1
            else:
                p.participant.vars['other_flag'] = random.randrange(1,Constants.num_flags,1)
            p.participant.vars['other_id'] = random.choice([i for  i  in choices2 if i != p.participant.vars['randomID']])

class Group(BaseGroup):
    pass

choices1= [["HQQkF10d","HQQkF10d"], ["pcrnTLUr","pcrnTLUr"], ["7OKdu5sV","7OKdu5sV"], ["wZPeexoH","wZPeexoH"], ["UkTbcudD","UkTbcudD"], ["zOz9aTis","zOz9aTis"], ["9MEcfOL3","9MEcfOL3"], ["SVwZaZ7E","SVwZaZ7E"], ["fFeJ8qw2","fFeJ8qw2"], \
    ["cRN5swzs","cRN5swzs"], ["ePrKx7Ma","ePrKx7Ma"], ["a1myqS0O","a1myqS0O"], ["b4RWtHe9","b4RWtHe9"], ["F8I03MH2","F8I03MH2"], ["C8feS7p2","C8feS7p2"], ["K4zdqslW","K4zdqslW"], ["3IbkRtps","3IbkRtps"], ["CiBI3ZYx","CiBI3ZYx"], ["9ME9zgnn","9ME9zgnn"], ["ZdIpJIRH","ZdIpJIRH"]]


#choices1= [[1,"HQQkF10d"], [2,"pcrnTLUr"], [3,"7OKdu5sV"], [4,"wZPeexoH"], [5,"UkTbcudD"], [6,"zOz9aTis"], [7,"9MEcfOL3"], [8,"SVwZaZ7E"], [9,"fFeJ8qw2"], [10,"cRN5swzs"],\
    # [11,"ePrKx7Ma"], [12,"a1myqS0O"], [13,"b4RWtHe9"], [14,"F8I03MH2"], [15,"C8feS7p2"], [16,"K4zdqslW"], [17,"3IbkRtps"], [18,"CiBI3ZYx"], [19,"9ME9zgnn"], [20,"ZdIpJIRH"]]
choices = random.choices(choices1, weights = None, k=3)



class Player(BasePlayer):
    my_ID = models.StringField(initial = 'initial')
    randomID = models.StringField(initial = 'initial') 
    customID = models.StringField(label = 'Please create your 8-character user ID.' )

    def customID_error_message(self, value):
        if len(value) != 8:
            return 'Chosen ID must have only 8 characters.'
        
    otherID = models.StringField(
        label = 'Please choose one of the following:',
        widget=forms.widgets.RadioSelect(choices=choices)
    )
    
    my_flag = models.IntegerField()

    show_ID = models.BooleanField(initial = False)

    def set_flag(self):
        index = self.my_flag
        self.my_flag = self.participant.vars['my_flag_choices'][index]
        
    def set_random_id(self):
        self.randomID = self.participant.vars['randomID']

    def set_ID(self,this):
        self.my_ID = this

    #adjective strings for evaluation page
    adj_1 = models.StringField()
    adj_2 = models.StringField()
    adj_3 = models.StringField()
    adj_4 = models.StringField(blank=True)
    adj_5 = models.StringField(blank=True)
    adj_6 = models.StringField(blank=True)
    adj_7 = models.StringField(blank=True)
    adj_8 = models.StringField(blank=True)
    adj_9 = models.StringField(blank=True)
    adj_10 = models.StringField(blank=True)

