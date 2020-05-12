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
    q_title = 'simple_survey_flag/q_title.html'
    both_IDs = 'simple_survey_flag/both_IDs.html'
    players_per_group = None
    num_rounds = 1
    num_flags = 25 #number of flags in _static file other than pride flag
    num_choices = 5 #number of flags a player can choose from other than pride flag
    flag_choices = [] # list of all flag choices
    for i in range(num_flags):
        flag_choices.append(i+1)

choices2= ["HQQkF10d","pcrnTLUr","7OKdu5sV","wZPeexoH","UkTbcudD","zOz9aTis","9MEcfOL3","SVwZaZ7E""fFeJ8qw2","cRN5swzs","ePrKx7Ma","a1myqS0O","b4RWtHe9","F8I03MH2","C8feS7p2","K4zdqslW","3IbkRtps","CiBI3ZYx","9ME9zgnn","ZdIpJIRH"]
consonants = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
id_choices = ['rzxw4' , 'wxzr4', 'zrwx4' ]
'''
for i in range(3):
    new_id = random.choice(consonants) + random.choice(consonants) + random.choice(consonants) + random.choice(consonants) + random.choice(consonants) + str(random.randrange(111,1000,1))
    id_choices.append(new_id)
'''

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            #p.participant.vars['my_flag_choices'] = Constants.flag_choices.copy()
            #random.shuffle(p.participant.vars['my_flag_choices'])
            #p.participant.vars['my_flag_choices'] = p.participant.vars['my_flag_choices'][:Constants.num_choices]
            #p.participant.vars['my_flag_choices'].append(Constants.num_flags + 1)
            #p.participant.vars['my_flag_choices'] = [11,17,20,22,25,26] #this line is just for hard-coded flag options. Lines above randomize from the list of all flags. Used until March 19th
            p.participant.vars['my_flag_choices'] = [11,17,26] #restricted as of March 19th to just three flags
            random.shuffle(p.participant.vars['my_flag_choices'])
            #p.participant.vars['randomID'] = random.choice(choices2)
            #p.participant.vars['randomID'] = random.choice(consonants) + random.choice(consonants) + random.choice(consonants) + random.choice(consonants) + random.choice(consonants)
            #p.participant.vars['randomID'] = p.participant.vars['randomID'] + str(random.randrange(111,1000,1))
            p.participant.vars['treat_assign'] = random.random()
            #p.participant.vars['other_id'] = random.choice(consonants) + random.choice(consonants) + random.choice(consonants) + random.choice(consonants) + random.choice(consonants)
            #p.participant.vars['other_id'] = p.participant.vars['other_id'] + str(random.randrange(111,1000,1))
            #p.participant.vars['other_id'] = random.choice([i for  i  in choices2 if i != p.participant.vars['randomID']])

class Group(BaseGroup):
    pass

choices1= [["HQQkF10d","HQQkF10d"], ["pcrnTLUr","pcrnTLUr"], ["7OKdu5sV","7OKdu5sV"], ["wZPeexoH","wZPeexoH"], ["UkTbcudD","UkTbcudD"], ["zOz9aTis","zOz9aTis"], ["9MEcfOL3","9MEcfOL3"], ["SVwZaZ7E","SVwZaZ7E"], ["fFeJ8qw2","fFeJ8qw2"], \
    ["cRN5swzs","cRN5swzs"], ["ePrKx7Ma","ePrKx7Ma"], ["a1myqS0O","a1myqS0O"], ["b4RWtHe9","b4RWtHe9"], ["F8I03MH2","F8I03MH2"], ["C8feS7p2","C8feS7p2"], ["K4zdqslW","K4zdqslW"], ["3IbkRtps","3IbkRtps"], ["CiBI3ZYx","CiBI3ZYx"], ["9ME9zgnn","9ME9zgnn"], ["ZdIpJIRH","ZdIpJIRH"]]


#choices1= [[1,"HQQkF10d"], [2,"pcrnTLUr"], [3,"7OKdu5sV"], [4,"wZPeexoH"], [5,"UkTbcudD"], [6,"zOz9aTis"], [7,"9MEcfOL3"], [8,"SVwZaZ7E"], [9,"fFeJ8qw2"], [10,"cRN5swzs"],\
    # [11,"ePrKx7Ma"], [12,"a1myqS0O"], [13,"b4RWtHe9"], [14,"F8I03MH2"], [15,"C8feS7p2"], [16,"K4zdqslW"], [17,"3IbkRtps"], [18,"CiBI3ZYx"], [19,"9ME9zgnn"], [20,"ZdIpJIRH"]]
#choices = random.choices(choices1, weights = None, k=3)



class Player(BasePlayer):
    consent = models.BooleanField(
        initial = False,
        label = '')
    my_ID = models.StringField(initial = 'initial')
    randomID = models.StringField(initial = 'initial') 
    customID = models.StringField(label = 'Please create your 8-character user ID.' )
    chooseID = models.StringField(
        label = 'Please choose one of the following IDs.',
        choices = id_choices,
        widget = forms.widgets.RadioSelect(),
        )
    
    def customID_error_message(self, value):
        if len(value) != 8:
            return 'Chosen ID must have only 8 characters.'

    
    my_flag = models.IntegerField()
    other_flag = models.IntegerField()
    
    show_ID = models.BooleanField(initial = False)

    part_vars = models.LongStringField()
    
    def set_flag(self):
        index = self.my_flag
        self.my_flag = self.participant.vars['my_flag_choices'][index]
        self.participant.vars['my_flag'] = self.my_flag
        
    def participant_vars_dump(self):
        self.part_vars = str(self.participant.vars)
        
    def set_other_flag(self):
        choices = [i for i in self.participant.vars['my_flag_choices'] if i!=Constants.num_flags+1 and i!=self.my_flag]

        if self.participant.vars['treat_assign'] <= 0.5:
            self.participant.vars['other_flag'] = Constants.num_flags + 1
            self.other_flag = self.participant.vars['other_flag']
            self.participant.vars['third_flag'] = random.choice(choices)
        else:
            self.participant.vars['other_flag'] = random.choice(choices)
            self.other_flag = self.participant.vars['other_flag']
            self.participant.vars['third_flag'] = Constants.num_flags + 1
        
    def set_random_id(self):
        self.randomID = self.participant.vars['randomID']

    def set_ID(self,this):
        self.my_ID = this
        self.participant.vars['my_ID'] = self.my_ID
        other_ID_choices = [i for i in id_choices if i != self.my_ID]
        self.participant.vars['other_id'] = random.choice(other_ID_choices)
        other_ID_choices = [i for i in other_ID_choices if i!= self.participant.vars['other_id']]
        self.participant.vars['third_id'] = random.choice(other_ID_choices)

    #adjective strings for evaluation page
    adj_1 = models.StringField(label = '')
    adj_2 = models.StringField(label = '')
    adj_3 = models.StringField(label = '')
    adj_4 = models.StringField(label = '',blank=True)
    adj_5 = models.StringField(label = '',blank=True)
    adj_6 = models.StringField(label = '',blank=True)
    adj_7 = models.StringField(label = '',blank=True)
    adj_8 = models.StringField(label = '',blank=True)
    adj_9 = models.StringField(label = '',blank=True)
    adj_10 = models.StringField(label = '',blank=True)

    #survey questions for second evaluation page
    inferred_gender = models.StringField(
        label = '',
        choices = ['Male','Female','Trans/Intersex/Other'],
        widget = forms.widgets.RadioSelect()
        )
    
    inferred_age = models.StringField(
        label = '',
        choices = ['Under 18','18 - 24','25 - 34', '35 - 44','45 - 54', '55 - 64','65 or Older'],
        widget = forms.widgets.RadioSelect()
        )
    
    inferred_income = models.StringField(
        label = '',
        choices = ['less than $20,000','$20,000 - $39,999','$40,000 - $59,999','$60,000 - $79,999','$80,000 - $99,999','$100,000 or more'],
        widget = forms.widgets.RadioSelect()
        )

    inferred_orientation = models.StringField(
        label = '',
        choices = ['Heterosexual or Straight', 'Non-heterosexual or Non-straight'],
        widget = forms.widgets.RadioSelect()
        )
    
    inferred_econ_politics = models.StringField(
        label = '',
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        widget = forms.widgets.RadioSelect()
        )
    
    inferred_social_politics = models.StringField(
        label = '',
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        widget = forms.widgets.RadioSelect()
        )
    
    inferred_ally = models.IntegerField(
        label = '',
        choices = [
                    [1,'Yes'],
                    [0,'No']
                   ],
        widget = forms.widgets.RadioSelect()
        )
    
    attn_check_3 = models.IntegerField(
        label = '(Attention Check) Please select 3 in the list below.',
        choices = [1,2,3,4,5],
        blank = True
        )

    ID_explain = models.LongStringField(initial = '', label = 'Why did you choose this ID? Please respond with at least 20 characters.')

    def ID_explain_error_message(self, value):
        if len(value) < 20:
            return 'Response must include at lease 20 characters.'

#higher order belief questions
    higher_inferred_ally = models.IntegerField(
        label = '',
        choices = [
                    [1,'Yes'],
                    [0,'No']
                   ],
        widget = forms.widgets.RadioSelect()
        )
    
    higher_inferred_gender = models.StringField(
        label = '',
        choices = ['Male','Female','Trans/Intersex/Other'],
        widget = forms.widgets.RadioSelect()
        )
    
    higher_inferred_orientation = models.StringField(
        label = '',
        choices = ['Heterosexual or Straight', 'Non-heterosexual or Non-straight'],
        widget = forms.widgets.RadioSelect()
        )

