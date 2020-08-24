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
    name_in_url = 'dg_qsp'
    players_per_group = None #pairs are made ex-post
    num_rounds = 2
    both_IDs = 'dg_qsp/both_IDs.html'
    instructions_template = 'dg_qsp/instructions.html'
    decision_template = 'dg_qsp/decision_template.html'

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
        choices = range(0,100,1)
        )
    
    attn_check_color = models.BooleanField(
        blank = True,
        choices = [
            [False,'Orange'],
            [True,'Red'],
            [False,'Blue']
            ],
        label = 'Please select the second option below',
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
        label = 'Please select the third option below',
        widget = forms.widgets.RadioSelect(),
        )

    def set_payoffs(self):
        self.gave = self.gave
        self.kept = Constants.endowment - self.gave
        self.payoff = self.kept
            

