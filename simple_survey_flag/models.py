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

doc = """
Survey (part 1) flag project
"""


class Constants(BaseConstants):
    name_in_url = 'simple_survey_flag'
    players_per_group = None
    num_rounds = 1


#class Subsession(BaseSubsession):
    #pass




class Group(BaseGroup):
    pass


choices1= [["HQQkF10d","HQQkF10d"], ["pcrnTLUr","pcrnTLUr"], ["7OKdu5sV","7OKdu5sV"], ["wZPeexoH","wZPeexoH"], ["UkTbcudD","UkTbcudD"], ["zOz9aTis","zOz9aTis"], ["9MEcfOL3","9MEcfOL3"], ["SVwZaZ7E","SVwZaZ7E"], ["fFeJ8qw2","fFeJ8qw2"], \
    ["cRN5swzs","cRN5swzs"], ["ePrKx7Ma","ePrKx7Ma"], ["a1myqS0O","a1myqS0O"], ["b4RWtHe9","b4RWtHe9"], ["F8I03MH2","F8I03MH2"], ["C8feS7p2","C8feS7p2"], ["K4zdqslW","K4zdqslW"], ["3IbkRtps","3IbkRtps"], ["CiBI3ZYx","CiBI3ZYx"], ["9ME9zgnn","9ME9zgnn"], ["ZdIpJIRH","ZdIpJIRH"]]

choices2= ["HQQkF10d","pcrnTLUr","7OKdu5sV","wZPeexoH","UkTbcudD","zOz9aTis","9MEcfOL3","SVwZaZ7E""fFeJ8qw2", \
    "cRN5swzs","ePrKx7Ma","a1myqS0O","b4RWtHe9","F8I03MH2","C8feS7p2","K4zdqslW","3IbkRtps","CiBI3ZYx","9ME9zgnn","ZdIpJIRH"]


#choices1= [[1,"HQQkF10d"], [2,"pcrnTLUr"], [3,"7OKdu5sV"], [4,"wZPeexoH"], [5,"UkTbcudD"], [6,"zOz9aTis"], [7,"9MEcfOL3"], [8,"SVwZaZ7E"], [9,"fFeJ8qw2"], [10,"cRN5swzs"],\
    # [11,"ePrKx7Ma"], [12,"a1myqS0O"], [13,"b4RWtHe9"], [14,"F8I03MH2"], [15,"C8feS7p2"], [16,"K4zdqslW"], [17,"3IbkRtps"], [18,"CiBI3ZYx"], [19,"9ME9zgnn"], [20,"ZdIpJIRH"]]
choices = random.choices(choices1, weights = None, k=3)



class Player(BasePlayer):
    randomID = models.StringField( ) #need to add button function
    customID = models.StringField(label = 'Please create your user ID' )
    otherID = models.IntegerField(
        #'Please choose one of the following:'
        #choices = random.choices(choices1, weights = None, k=3)
        widget=forms.widgets.CheckboxSelectMultiple(choices=choices)    
    )
    flag = models.IntegerField(label = 'Please enter a number corresponding to the profile image of your choice', min = 1, max = 3)


class Subsession(BaseSubsession):
    def creating_session(self):
        for P in self.get_players():
            P.randomID = random.choice(choices2)
            print('Your randomly generated ID', P.randomID)

 #participant.vars.
            
