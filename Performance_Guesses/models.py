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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Performance_Guesses'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    belief_game_1 = models.IntegerField(widget=widgets.RadioSelect,
        choices=[
            [1, 'The best performer in your group.'],
            [2, 'The second best performer in your group.'],
            [3, 'The third best performer in your group.'],
            [4, 'The fourth best (the worst) performer in your group.']
        ]
    )
    belief_game_2 = models.IntegerField(widget=widgets.RadioSelect,
        choices=[
            [1, 'The best performer in your group.'],
            [2, 'The second best performer in your group.'],
            [3, 'The third best performer in your group.'],
            [4, 'The fourth best (the worst) performer in your group.']
        ]
    )
    pass
