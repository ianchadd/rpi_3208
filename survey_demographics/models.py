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
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    state_list = ['Alaska', 'Alabama', 'Arkansas', 'American Samoa', 'Arizona', 'California', 'Colorado', 'Connecticut',
                  'District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Iowa', 'Idaho', 'Illinois',
                  'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota',
                  'Missouri', 'Northern Mariana Islands', 'Mississippi', 'Montana', 'National', 'North Carolina', 'North Dakota',
                  'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon',
                  'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
                  'Virginia', 'Virgin Islands', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming', 'N/A']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#age
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    yob = models.StringField(
        label='What is your year of birth?',
        )
    def yob_error_message(self,value):
        if len(value) !=4:
            return 'You must enter a valid year of birth in the format YYYY.'
        
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
        blank = True)
    t_male = models.BooleanField(
        label = 'Trans male / Trans man',
        widget=widgets.CheckboxInput,
        blank = True)
    t_female = models.BooleanField(
        label = 'Trans female / Trans woman',
        widget=widgets.CheckboxInput,
        blank = True)
    gnc = models.BooleanField(
        label = 'Genderqueer / Gender non-conforming',
        widget=widgets.CheckboxInput,
        blank = True)
    diff_gend = models.StringField(
        label = 'Different identity?',
        blank = True)
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
        blank = True
        )
#sexual history and attraction
    sex_hist = models.StringField(
        label = 'In the past year, who have you had sex with?',
        choices = [
            'Men only',
            'Women only',
            'Both men and women',
            'I have not had sex'],
        widget = widgets.RadioSelect,
        )
    attracted_men = models.BooleanField(
        label = 'Are you sexually attracted to men?',
        choices = [[True,'Yes'][False,'No']],
        widget = widgets.RadioSelect,
        )
    attracted_women = models.BooleanField(
        label = 'Are you sexually attracted to women?',
        choices = [[True,'Yes'][False,'No']],
        widget = widgets.RadioSelect,
        )
#relationship status
    relationship = models.StringField(
        label = 'Please indicate your current relationship status',
        choices = [
            'Single',
            'Domestic Partnership (living in the same home)',
            'Partnership (not living in the same home)',
            'Married',
            'Other (please indicate below)'
            ]
        widget = widgets.RadioSelect
        )
    other_relationship = models.StringField(
        label = '',
        blank = True)
    primary_earner = models.StringField(
        label = 'Are you the primary earner in the household?',
        choices = [
            'Yes',
            'No',
            'Multiple primary earners in household'
            ]
        widget = widgets.RadioSelect
        )
#income
    income = models.StringField(
        label = "Please select your household annual income from the options below",
        choices = ['less than $20,000','$20,000 - $40,000','$40,000 - $60,000','$60,000 - $80,000','$80,000 - $100,000','More than $100,000'],
        widget = forms.widgets.RadioSelect()
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
            'Other (please enter below)'
            ]
        widget = widgets.RadioSelect
        )
    other_ethinicity = models.StringField(
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
            ]
        widget = widgets.RadioSelect
        )
    other_religion = models.StringField(
        label = '',
        blank = True
        )
    
#politics
    politics = models.StringField(
        label = "Politically, I am",
        choices = ['More conservative than liberal', 'Equally conservative and liberal', 'More liberal than conservative'],
        widget = forms.widgets.RadioSelect()
        )
#locations
    live_in = models.StringField(
        label = 'In which US state/territory do you currently live?',
        choices = Constants.state_list
        )
    grew_up_in = models.StringField(
        label = 'In which US state/territory did you spend the most time in as a child?',
        choices = Constants.state_list
        )
        
        
