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
    name_in_url = 'Game_3'
    players_per_group = None
    num_rounds = 1
    round_values = ["0.25","0.50","0.75","1.00","1.25","1.50","1.75"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attention_check = models.BooleanField(
        label = 'This question is to check your attention. Please select Option 1 below',
        choices = [
            [True, 'Option 1'],
            [False, 'Option 2']
            ],
        blank = True,
        )

    game_3_switch = models.FloatField(
        label = '',
        widget = widgets.RadioSelect
    )

    def game_3_switch_choices(self):
        round_values = [float(i) for i in Constants.round_values]
        round_values.append(round_values[-1]+0.001)
        choices = []
        for i in range(len(round_values)):
            if i == 0:
                choices.append([round_values[i],'I would like to enter the tournament no matter what the tournament prize is.'])
            elif i == len(round_values) - 1:
                choices.append([round_values[i],'I would not like to enter the tournament no matter what the tournament prize is.'])
            elif i == len(round_values) - 2:
                choices.append([round_values[i],'I would like to enter the tournament if the tournament prize is $'+str(round_values[i])+'.'])
            else:
                choices.append([round_values[i],'I would like to enter the tournament if the tournament prize is $'+str(round_values[i])+' or higher.'])
        return choices
