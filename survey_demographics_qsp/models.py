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
    
class Constants(BaseConstants):
    name_in_url = 'survey_qsp'
    players_per_group = None
    num_rounds = 1
    
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
state_list = []
for key in states:
    if key != 'NA':
        state_list.append(key + ' (' + states[key] + ')')

live_state_list = state_list + ['Other (please state below)']
grew_up_state_list = state_list + ['Other (please state below)']

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#age
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    yob = models.IntegerField(
        label='What is your year of birth?',
        min=1900,
        max=2005
        )
        
#sex assigned at birth 
    sex = models.StringField(
        label = 'What sex were you assigned at birth, on your original birth certificate?',
        choices = ['Male', 'Female']
        )
#gender
    male = models.BooleanField(
        label = 'Male',
        widget=widgets.CheckboxInput,
        blank = True)
    female = models.BooleanField(
        label = 'Female',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    t_male = models.BooleanField(
        label = 'Trans male / Trans man',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    t_female = models.BooleanField(
        label = 'Trans female / Trans woman',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    gnc = models.BooleanField(
        label = 'Genderqueer / Gender non-conforming',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    nb = models.BooleanField(
        label = 'Nonbinary',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    other_g = models.BooleanField(
        label = 'Other (please state below)',
        widget=widgets.CheckboxInput,
        initial = False,
        blank = True)
    diff_gend = models.StringField(
        label = '',
        initial = '',
        blank = True)

    def diff_gend_error_message(self,value):
        if self.other_g and type(value) == type(None):
            return 'If you select Other, you must specify in the provided field'
            
#sexual orientation
    orientation = models.StringField(
        label = 'Which do you consider yourself to be:',
        choices = [
            'Heterosexual or straight',
            'Gay or lesbian',
            'Bisexual',
            'Other (please state below)'
            ],
        widget = widgets.RadioSelect,
        )
    other_orientation = models.StringField(
        label = '',
        initial = '',
        blank = True
        )
#sexual history and attraction
    sex_hist = models.StringField(
        label = 'In the past year, who have you had sex with?',
        choices = [
            'Men only',
            'Women only',
            'Both men and women',
            'I have not had sex',
            'I prefer not to say'],
        widget = widgets.RadioSelect,
        )
    attracted_men = models.BooleanField(
        label = 'Are you sexually attracted to men?',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
    attracted_women = models.BooleanField(
        label = 'Are you sexually attracted to women?',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
    relations_same = models.BooleanField(
        label='',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
    relations_different = models.BooleanField(
        label='',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
    attraction_same = models.BooleanField(
        label='',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
    attraction_different = models.BooleanField(
        label='',
        choices = [[True,'Yes'],[False,'No']],
        widget = widgets.RadioSelect,
        )
    
#education
    education = models.StringField(
        label = 'What is the highest education level you have attained?',
        choices = [
            'Did not complete High School',
            'Graduated from High School',
            'Some College',
            "Bachelor's Degree",
            "Master's Degree",
            "PhD or Higher"
            ]
        )
        
#relationship status
    relationship = models.StringField(
        label = 'Please indicate your current relationship status',
        choices = [
            'Single',
            'Partnership (not living in the same home)',
            'Domestic Partnership (living in the same home)',
            'Married',
            'Other (please state below)'
            ],
        widget = widgets.RadioSelect
        )
    other_relationship = models.StringField(
        label = '',
        initial = '',
        blank = True)
    primary_earner = models.StringField(
        label = 'Are you the primary earner in the household?',
        choices = [
            'Yes',
            'No',
            'Multiple primary earners in household'
            ],
        widget = widgets.RadioSelect
        )
#income
    income = models.StringField(
        label = "Please select your household annual income from the options below",
        choices = ['less than $20,000','$20,000 - $39,999','$40,000 - $59,999','$60,000 - $79,999','$80,000 - $99,999','$100,000 or more'],
        widget = widgets.RadioSelect
        )
        
#race
    ethnicity = models.StringField(
        label='What is your ethnicity?',
        choices = [
            'White',
            'Black or African American',
            'American Indian and Alaskan Native',
            'Asian',
            'Native Hawaiian or Pacific Islander',
            'Hispanic or Latino',
            'Middle Eastern or Arab',
            'Other (please state below)'
            ],
        widget = widgets.RadioSelect
        )
    other_ethnicity = models.StringField(
        label = '',
        blank = True
        )
#religion
    religion = models.StringField(
        label = 'What is your religious affiliation?',
        choices = [
            'Christian (any denomination)',
            'Hindu',
            'Buddhist',
            'Jewish',
            'Muslim',
            'Asian Folk Religion (e.g. Taoist, Confucian)',
            'I am not religious',
            'Some other religious affiliation (please specify below)'
            ],
        widget = widgets.RadioSelect
        )
    other_religion = models.StringField(
        label = '',
        blank = True
        )
    
#politics
    econ_politics = models.StringField(
        label = '',
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        widget = widgets.RadioSelect
        )
    
    social_politics = models.StringField(
        label = '',
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        widget = widgets.RadioSelect
        )
        
#care about what others think
    care_others = models.IntegerField(
        label = 'To what extent do you agree with the following statement: "I care about what others think of my actions."',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )
        
#lgbt_attitude
    #used in Aksoy et al. EER paper
    lgbt_free = models.IntegerField(
        label = 'To what extent do you agree with the following statement: "Gay men and lesbians should be free to live their own lives as they wish."',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )
    lgbt_discrim = models.IntegerField(
        label = 'To what extent do you agree with the following statement: "It should be legal for business owners to refuse to serve same-sex partners."',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )
    lgbt_adopt = models.IntegerField(
        label = 'To what extent do you agree with the following statement: "It should be legal for same-sex partners to adopt a child."',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )
    lgbt_marriage = models.IntegerField(
        label = 'To what extent do you agree with the following statement: "Marriages between same-sex partners should be recognized by the law as valid, with the same rights as traditional marriages."',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )
    lgbt_bathroom = models.IntegerField(
        label = 'To what extent do you agree with the following statement: "Transgender people should have to use the bathroom/locker rooms of the sex they were assigned at birth."',
        choices = [[5,'Strongly Agree'],
                   [4,'Agree'],
                   [3,'Neither Agree nor Disagree'],
                   [2,'Disagree'],
                   [1,'Strongly Disagree']
                   ],
        widget = widgets.RadioSelect
        )
        
#lgbt friend
    lgbt_friend = models.BooleanField(
        label = 'Do you have a close friend or family member who identifies as LGBTQ+?',
        choices = [
            [True, 'Yes'],
            [False, 'No']
            ],
        widget = widgets.RadioSelect
        )
    lgbt_met = models.BooleanField(
        label = 'Have you ever met someone who identifies as LGBTQ+?',
        choices = [
            [True, 'Yes'],
            [False, 'No']
            ],
        widget = widgets.RadioSelect
        )

    
#locations
    live_in = models.StringField(
        label = 'In which US state/territory do you currently live?',
        choices = live_state_list
        )
    grew_up_in = models.StringField(
        label = 'In which US state/territory did you spend the most time in for the first 18 years of your life?',
        choices = grew_up_state_list
        )
    other_live_location = models.StringField(
        label = '',
        blank = True
        )
    other_grew_up_location = models.StringField(
        label = '',
        blank = True
        )
#attention check
    attn_check_1 = models.IntegerField(
        label = 'Please select 1 in the list below.',
        choices = [1,2,3,4,5],
        blank = True
        )
    
#allyship questions
    consider_lgbt_ally = models.IntegerField(
        label = 'Do you consider yourself to be an ally to the LGBTQ+ community?',
        choices = [[1, 'Yes'],[0,'No']],
        widget = widgets.RadioSelect
        )
    program_lgbt_ally = models.IntegerField(
        label = 'Are you formally registered as an LGBTQ+ ally (e.g. Safe Zone Training, Campus Ally programs, etc.) in your workplace, school, university, or other institution?',
        choices = [[1, 'Yes'],[0,'No']],
        widget = widgets.RadioSelect
        )

#prolific guesses
    prolific_female = models.StringField(
        label = 'Which of the following best describes your opinion?',
        choices = [
            ['<','I think less than 51% of the Prolific participants are female'],
            ['=','I think about 51% of the Prolific participants are female'],
            ['>','I think more than 51% of the Prolific participants are female'],
            ],
        widget = widgets.RadioSelect
        )
    prolific_lgbt = models.StringField(
        label = 'Which of the following best describes your opinion?',
        choices = [
            ['<','I think less than 5% of the Prolific participants identify as LGBT'],
            ['=','I think about 5% of the Prolific participants identify as LGBT'],
            ['>','I think more than 5% of the Prolific participants identify as LGBT'],
            ],
        widget = widgets.RadioSelect
        )
    prolific_ally = models.IntegerField(
        label = 'What percentage of Prolific participants do you think are allies to the LGBTQ+ community? Please enter a number between 0 and 100',
        min=0,
        max=100,
        )
    prolific_liberal = models.IntegerField(
        label = 'Percentage of Prolific participants who are more liberal than conservative on social issues',
        min=0,
        max=100,
        )
    prolific_equal = models.IntegerField(
        label = 'Percentage of Prolific participants who are equally liberal and conservative on social issues',
        min=0,
        max=100,
        )
    prolific_conservative = models.IntegerField(
        label = 'Percentage of Prolific participants who are less liberal than conservative on social issues',
        min=0,
        max=100,
        )
