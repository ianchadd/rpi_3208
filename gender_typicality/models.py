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
import random




class Constants(BaseConstants):
    name_in_url = 'gt'
    players_per_group = None
    num_rounds = 50


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number==1:
            for p in self.get_players():
                p.participant.vars['num_questions'] = len(self.session.config['questions'])
                p.participant.vars['questions']=self.session.config['questions']
                if self.session.config['random']:
                    random.shuffle(p.participant.vars['questions']) #for random question order


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    arrested = models.BooleanField(
        label = 'Have you ever been arrested?',
        choices = [
            [False, 'No'],
            [True, 'Yes'],
            ],
        widget = widgets.RadioSelect
        )
    intelligent = models.IntegerField(
        label = "Compared to other people your age, how intelligent are you?",
        choices = [
            [1, 'Moderately below'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, 'Extremely above'],
            ],
        widget = widgets.RadioSelect
        )
    imagination = models.IntegerField(
        label = 'I have a vivid imagination',
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    military = models.BooleanField(
        label = 'Have you ever been in the military?',
        choices = [
            [False, 'No'],
            [True, 'Yes'],
            ],
        widget = widgets.RadioSelect
        )
    mood = models.IntegerField(
        label = 'I have frequent mood swings',
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    others_problems = models.IntegerField(
        label = "I am not interested in other people's problems",
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    others_interested = models.IntegerField(
        label = "I am not really interested in others",
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    pray = models.IntegerField(
        label = "How often do you pray privately?",
        choices = [
            [0, 'Not at all'],
            [1, '1 time'],
            [2, '2 times'],
            [3, '3 times'],
            [4, '4 times'],
            [5, '5 times'],
            [6, '6 times'],
            [7, 'More than once a day']
            ],
        widget = widgets.RadioSelect
        )
    risks = models.IntegerField(
        label = "I like to take risks",
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    stress = models.IntegerField(
        label = "I get stressed out easily",
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    sun = models.IntegerField(
        label = "During a typical summer week, how many hours do you spend in the sun during the day?",
        min=0,
        max=99
        )
    sunblock = models.IntegerField(
        label = 'When you go outside on a sunny day for more than one hour, how likely aare you to use sunscreen or sunblock?',
        choices = [
            [1, 'Very likely'],
            [2, ''],
            [3, 'Unlikely']
            ],
        widget = widgets.RadioSelect
        )
    strength = models.IntegerField(
        label = "In an average week, how many times do you participate in gymnastics, weight lifting, or strength training?",
        choices = [
            [0, 'Not at all'],
            [1, '1 time'],
            [2, '2 times'],
            [3, '3 times'],
            [4, '4 times'],
            [5, '5 times'],
            [6, '6 times'],
            [7, '7 or more times']
            ],
        widget = widgets.RadioSelect
        )
    sweat = models.BooleanField(
        label = 'In the past 24h, have you participated in vigorous activity long enough to work up a sweat, get your heart thumping, or get out of breath?',
        choices = [
            [False, 'No'],
            [True, 'Yes'],
            ],
        widget = widgets.RadioSelect
        )
    team_sports = models.IntegerField(
        label = "In an average week, how many time do you participate in strenuous team sports such as football, soccer, basketball, lacrosse, rugby, field hockey, or ice hockey?",
        choices = [
            [0, 'Not at all'],
            [1, '1 time'],
            [2, '2 times'],
            [3, '3 times'],
            [4, '4 times'],
            [5, '5 times'],
            [6, '6 times'],
            [7, '7 or more times']
            ],
        widget = widgets.RadioSelect
        )
    tired = models.IntegerField(
        label = 'In an average week, you feel too tired to do things',
        choices = [
            [0, 'Never or rarely'],
            [1, ''],
            [2, ''],
            [3, 'Most or all of the time']
            ],
        widget = widgets.RadioSelect
        )
    walk = models.IntegerField(
        label = "In an average week, how many times do you walk for exercise?",
        choices = [
            [0, 'Not at all'],
            [1, '1 time'],
            [2, '2 times'],
            [3, '3 times'],
            [4, '4 times'],
            [5, '5 times'],
            [6, '6 times'],
            [7, '7 or more times']
            ],
        widget = widgets.RadioSelect
        )
    sympathize = models.IntegerField(
        label = "I sympathize with others' feelings",
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    talk = models.IntegerField(
        label = "I don't talk a lot",
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )
    tobacco = models.BooleanField(
        label = 'Have you ever used chewing tobacco at least 20 times in your entire life?',
        choices = [
            [False, 'No'],
            [True, 'Yes'],
            ],
        widget = widgets.RadioSelect
        )
    video_games = models.IntegerField(
        label = "Hours per week playing video/computer games",
        min=0,
        max=150
        )
    worry = models.IntegerField(
        label = "I worry about things",
        choices = [
            [1, 'Strongly agree'],
            [2, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [4, 'Disagree'],
            [5, 'Strongly disagree']
            ],
        widget = widgets.RadioSelect
        )

    
