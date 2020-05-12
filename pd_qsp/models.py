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
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'pd_qsp/instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(10)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(7)
    both_defect_payoff = c(1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision_first = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label = 'I choose',
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    decision_second = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label = 'I choose',
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
