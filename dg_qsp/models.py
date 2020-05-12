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
    num_rounds = 1
    both_IDs = 'dg_qsp/both_IDs.html'
    instructions_template = 'dg_qsp/instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    kept = models.CurrencyField(
    doc="""Amount dictator decided to keep for himself""",
    min=0,
    max=Constants.endowment,
    )
    gave = models.CurrencyField()

    def set_payoffs(self):
        self.payoff = self.kept
        self.gave = Constants.endowment - self.kept
