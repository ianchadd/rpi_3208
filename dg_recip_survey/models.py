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


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'dg_recip'
    players_per_group = None #pairs are made ex-post
    num_rounds = 1
    instructions_template = 'dg_recip_survey/instructions.html'
    decision_template = 'dg_recip_survey/decision_template.html'

    # Initial amount allocated to the dictator
    endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def participant_vars_dump(self, page):
        for field in page.form_fields:
            if type(getattr(self, field)) != type(None):
                if Constants.num_rounds > 1:
                    self.participant.vars[field +'_'+str(self.round_number)] = getattr(self, field)
                else:
                    self.participant.vars[field] = getattr(self, field)
            
    kept = models.IntegerField(
    doc="""Amount dictator decided to keep for himself""",
    )
    gave = models.IntegerField(
        min=0,
        max=100,
        )
    
    attn_check_color = models.BooleanField(
        blank = True,
        choices = [
            [False,'Orange'],
            [True,'Red'],
            [False,'Blue']
            ],
        label = 'This is to check your attention. Please select the second option below',
        widget = forms.widgets.RadioSelect(),
        )
    
    attn_check_color_2 = models.BooleanField(
        blank = True,
        choices = [
            [False,'Red'],
            [False,'Blue'],
            [True,'White'],
            [False, 'Black']
            ],
        label = 'This is to check your attention. Please select the third option below',
        widget = forms.widgets.RadioSelect(),
        )
    
    check_understanding = models.BooleanField(
        blank = False,
        choices = [True, False],
        label = '',
        widget = forms.widgets.RadioSelect(),
        )

    check_understanding_mistakes = models.IntegerField(
        initial = 0
        )

    def check_understanding_error_message(self,value):
        if value:
            self.check_understanding_mistakes += 1
            return 'This statement is false. Remember that your bonus payment from this part of Task 2 is the sum of the amounts that ALL your matched partners choose to allocate to you.'
            

