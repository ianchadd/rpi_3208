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
    players_per_group = None
    num_rounds = 1
    num_flags = 50 #number of flags in _static file other than pride flag
    num_choices = 5 #number of flags a player can choose from other than pride flag
    flag_choices = [] # list of all flag choices
    for i in range(num_flags):
        flag_choices.append(i+1)


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['my_flag_choices'] = Constants.flag_choices.copy()
            random.shuffle(p.participant.vars['my_flag_choices'])
            p.participant.vars['my_flag_choices'] = p.participant.vars['my_flag_choices'][:Constants.num_choices]
            p.participant.vars['my_flag_choices'].append(Constants.num_flags + 1)
            random.shuffle(p.participant.vars['my_flag_choices'])


class Group(BaseGroup):
    pass

choices1= [["HQQkF10d","HQQkF10d"], ["pcrnTLUr","pcrnTLUr"], ["7OKdu5sV","7OKdu5sV"], ["wZPeexoH","wZPeexoH"], ["UkTbcudD","UkTbcudD"], ["zOz9aTis","zOz9aTis"], ["9MEcfOL3","9MEcfOL3"], ["SVwZaZ7E","SVwZaZ7E"], ["fFeJ8qw2","fFeJ8qw2"], \
    ["cRN5swzs","cRN5swzs"], ["ePrKx7Ma","ePrKx7Ma"], ["a1myqS0O","a1myqS0O"], ["b4RWtHe9","b4RWtHe9"], ["F8I03MH2","F8I03MH2"], ["C8feS7p2","C8feS7p2"], ["K4zdqslW","K4zdqslW"], ["3IbkRtps","3IbkRtps"], ["CiBI3ZYx","CiBI3ZYx"], ["9ME9zgnn","9ME9zgnn"], ["ZdIpJIRH","ZdIpJIRH"]]

#choices1= [[1,"HQQkF10d"], [2,"pcrnTLUr"], [3,"7OKdu5sV"], [4,"wZPeexoH"], [5,"UkTbcudD"], [6,"zOz9aTis"], [7,"9MEcfOL3"], [8,"SVwZaZ7E"], [9,"fFeJ8qw2"], [10,"cRN5swzs"],\
    # [11,"ePrKx7Ma"], [12,"a1myqS0O"], [13,"b4RWtHe9"], [14,"F8I03MH2"], [15,"C8feS7p2"], [16,"K4zdqslW"], [17,"3IbkRtps"], [18,"CiBI3ZYx"], [19,"9ME9zgnn"], [20,"ZdIpJIRH"]]
choices = random.choices(choices1, weights = None, k=3)



class Player(BasePlayer):
    randomID = models.StringField(label = 'temporary input field, will be changed to just randomly assigning a string') #need to turn this into a randomly generated number
    customID = models.StringField(label = 'Please create your user ID' )
    otherID = models.StringField(
        label = 'Please choose one of the following:',
        #choices = random.choices(choices1, weights = None, k=3)
        widget=forms.widgets.RadioSelect(choices=choices)
    )
    my_flag = models.IntegerField()

    def set_flag(self):
        index = self.my_flag
        self.my_flag = self.participant.vars['my_flag_choices'][index]
