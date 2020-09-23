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
    name_in_url = 'Game_4'
    players_per_group = None
    num_rounds = 1
    round_values = ["0.25","0.50","0.75","1.00","1.25","1.50","1.75"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attention_check = models.BooleanField(
        label = 'This question is to check your attention. Please select Option 2 below',
        choices = [
            [False, 'Option 1'],
            [True, 'Option 2'],
            [False, 'Option 3'],
            [False, 'Option 4']
            ],
            blank=True
        )
    game_4_switch = models.FloatField(
        label = 'Would you like the tournament payment scheme to apply to your past performance in Game-1?',
        widget = widgets.RadioSelect
    )

    def game_4_switch_choices(self):
        round_values = [float(i) for i in Constants.round_values]
        round_values.append(round_values[-1]+0.001)
        choices = []
        for i in range(len(round_values)):
            if i == 0:
                choices.append([round_values[i],'Yes, I prefer the tournament scheme no matter what the tournament prize is.'])
            elif i == len(round_values) - 1:
                choices.append([round_values[i],'No, I prefer the piece rate scheme no matter what the tournament prize is.'])
            elif i == len(round_values) - 2:
                choices.append([round_values[i],'Yes, only if the tournament prize is $'+str("{:.2f}".format(round_values[i]))+'. Otherwise, I prefer the piece rate scheme.'])
            else:
                choices.append([round_values[i],'Yes, only if the tournament prize is $'+str("{:.2f}".format(round_values[i]))+' or higher. Otherwise, I prefer the piece rate scheme'])
        return choices
