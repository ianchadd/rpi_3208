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
    num_rounds = 2
    instructions_template = 'dg_recip_survey/instructions.html'
    decision_template = 'dg_recip_survey/decision_template.html'

    # Initial amount allocated to the dictator
    endowment = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    kept = models.CurrencyField(
    doc="""Amount dictator decided to keep for himself""",
    )
    gave = models.CurrencyField(
        choices = currency_range(c(0),c(100), c(1))
        )
    
    attn_check_color = models.IntegerField(
        blank = True,
        choices = [
            [1,'Orange'],
            [2,'Red'],
            [3,'Blue']
            ],
        label = 'Please select the second option below',
        widget = forms.widgets.RadioSelect(),
        )
    
    attn_check_color_2 = models.IntegerField(
        blank = True,
        choices = [
            [1,'Red'],
            [2,'Blue'],
            [3,'White'],
            [4, 'Black']
            ],
        label = 'Please select the third option below',
        widget = forms.widgets.RadioSelect(),
        )

    def set_payoffs(self):
        self.gave = self.gave
        self.kept = Constants.endowment - self.gave
        self.payoff = self.kept
        self.participant.vars['gave_'+str(self.round_number)] = self.gave
        self.participant.vars['kept_'+str(self.round_number)] = self.kept
            

