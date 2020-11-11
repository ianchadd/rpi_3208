from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import ast
option_value_list = []
with open("_static/no_choice/options_input.csv", newline='') as csvfile:
    my_list = csv.reader(csvfile, delimiter=',')
    for row in my_list:
        option_value_list.append(row)
empty = {''}
for i in range(len(option_value_list)):
    option_value_list[i] = [j for j in option_value_list[i] if len(j) > 0 and len(j) < 20]


class Constants(BaseConstants):
    name_in_url = 'nbo_choice'
    players_per_group = None
    option_values = option_value_list
    num_rounds = len(option_values)
    #num_rounds = 3
    nbo_value = 14
    num_options = 10
    num_attributes = 50
    pay_attribute = '#'
    timeout = 120 #set at 2 minutes for now as a bookmark


class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools
        treats = itertools.cycle(['baseline','nbo']) #no choice refers to baseline and choice refers to having NBO
        #with exogenous treatment, treat == 'exo'; set in the session configuration
        for p in self.get_players():
            p.participant.vars['treat'] = next(treats) #sets treatment var at participant level with balanced treatment
            if 'treat' in self.session.config:
                p.participant.vars['treat'] = self.session.config['treat']
            p.participant.vars['order'] = list(range(1,Constants.num_rounds + 1))
            random.shuffle(p.participant.vars['order'])
            rounds = list(range(1,Constants.num_rounds + 1))
            random.shuffle(rounds)
            p.participant.vars['pay_round'] = rounds[0]
            p.participant.vars['points_per_dollar'] = int(1/self.session.config['real_world_currency_per_point'])
            nbo_choices = []
            for i in range(Constants.num_rounds):
                nbo_choices.append(random.choice([False,True]))
            p.participant.vars['nbo_choices'] = nbo_choices


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #value of chosen object, default is zero
    value = models.IntegerField(initial=0)

    nbo_choice = models.BooleanField(
            choices=[
                [False, 'I want to choose for myself, show me my options'],
                [True, 'I want to take the outside option of ' + str(Constants.nbo_value) + ' points'],

            ],
        label='Would you like to take the outside option?',
        widget=widgets.RadioSelect)

    option_values = models.StringField()

    option_choose = models.IntegerField()

    def option_choose_error_message(self,value):
        if type(value) == type(None):
            return 'You must select one of the displayed options.'

    round_max = models.IntegerField()

    correct = models.BooleanField()

    def exo_outside_option(self):
        self.nbo_choice = self.participant.vars['nbo_choices'][self.round_number - 1]

    def set_option_values(self):
        self.option_values = str(Constants.option_values[self.participant.vars['order'][self.round_number-1]-1])

    def set_round_max(self):
        vals = self.option_values
        vals = ast.literal_eval(vals)
        vals = [int(i) for i in vals]
        vals.sort()
        self.round_max = vals[-1]

    def set_correct(self):
        self.correct = self.value == self.round_max

    def set_value(self):
        if self.nbo_choice:
            self.value = Constants.nbo_value
        else:
            self.value = int(Constants.option_values[self.participant.vars['order'][self.round_number-1]-1][self.option_choose - 1])

    def set_payoff(self):
        if self.round_number == self.participant.vars['pay_round']:
            self.payoff = self.value
        else:
            self.payoff = 0
