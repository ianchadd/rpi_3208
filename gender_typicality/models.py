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
    num_rounds = 1


class Subsession(BaseSubsession):
    pass 
   # def creating_session(self):
   #     if self.round_number==1:
   #         for p in self.get_players():
   #             p.participant.vars['num_questions'] = len(self.session.config['questions'])
   #             p.participant.vars['questions']=self.session.config['questions']
   #             if self.session.config['random']:
   #                 random.shuffle(p.participant.vars['questions']) #for random question order


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    



    work_house = models.IntegerField(
        label = "In an average week, how many times do you do work around the house?",
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

    gymnastics = models.IntegerField(
        label = "In an average week, how many times do you participate in gymnastics, weight lifting or strength training?",
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



    roller_blade = models.IntegerField(
        label = "In an average week, how many times do you roller blade, roller skate, downhill ski, snow board, play racquet sports, or do aerobics?",
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



    strenuous = models.IntegerField(
        label = "In an average week, how many times do you participate in strenuous team sports such as football, soccer, basketball, lacrosse, rugby, field hockey, or ice hockey?",
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



    walk = models.IntegerField(
        label = "In an average week, how many times do you walk for exercise",
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



    bike = models.IntegerField(
        label = "In an average week, how many times do you bike/skate/dance/skateboard?",
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



    talk = models.IntegerField(
        label = "In an average week, how many times do you hang with friends or talk on the telephone for more than 5 min?",
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



    tv = models.IntegerField(
        label = "In an average week, how many times do you watch TV?",
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
    
    hobby = models.IntegerField(
        label = "In an average week, how many times do you engage in a hobby such as working on a collection, playing cards or board games, arts and crafts, dram a, playing a musical instrument or singing with a group, or shopping just for fun?",
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

    sad = models.IntegerField(
        label = "In an average week, how often do you feel sad?",
        choices = [
            [0, 'Never or rarely'],
            [1, 'Sometimes'],
            [2, 'A lot of the time'],
            [3, 'Most of the time or all of the time']
            ],
        widget = widgets.RadioSelect
        )

    tired = models.IntegerField(
        label = "In an average week, how often do you feel too tired to do things?",
        choices = [
            [0, 'Never or rarely'],
            [1, 'Sometimes'],
            [2, 'A lot of the time'],
            [3, 'Most of the time or all of the time']
            ],
        widget = widgets.RadioSelect
        )

    video_games = models.IntegerField(
        label = "In an average week, how many hours do you spend playing video or computer games, or using a computer? Do not count computer use for work or school.",
        min=0,
        max=105
        )



    
    damage = models.IntegerField(
        label = "In the past 12 months, how often deliberately did you damage property that wasn’t yours?",
        choices = [
            [0, 'Not at all'],
            [1, '1 or 2 times'],
            [2, '3 or 4 times'],
            [3, '5 or more times'],
            ],
        widget = widgets.RadioSelect
        )
    fight  = models.IntegerField(
        label = "In the past 12 months, how often did you take part in physical fight where your group against another group?",
        choices = [
            [0, 'Not at all'],
            [1, '1 or 2 times'],
            [2, '3 or 4 times'],
            [3, '5 or more times'],
            ],
        widget = widgets.RadioSelect
        )
    substance = models.IntegerField(
        label = "In the past 12 months, have you used a legal performance-enhancing substance for athletes (such as Creatine, Monohydrate, or Andro)?",
        choices = [
            [1, 'Yes'],
            [2, 'No'],
            ],
        widget = widgets.RadioSelect
        )



    weight  = models.IntegerField(
        label = "What do you think of yourself in terms of weight?",
        choices = [
            [1, 'Very underweight'],
            [2, 'Slightly underweight'],
            [3, 'About the right weight'],
            [4, 'Slightly overweight'],
            [5, 'Very overweight'],
            ],
        widget = widgets.RadioSelect
        )


    stretching  = models.IntegerField(
        label = 'How true is the following statement: I can do a good job stretching the truth when I talk to people.',
        choices = [
            [1, 'Not true'],
            [2, 'A little true'],
            [3, 'Somewhat true'],
            [4, 'Pretty true'],
            [5, 'Very true'],
            ],
        widget = widgets.RadioSelect
        )

    gun = models.BooleanField(
        label = 'Do you own a handgun?',
        choices = [
            [True, 'Yes'],
            [False, 'No'],
            ],
        widget = widgets.RadioSelect
        )

    sunblock = models.IntegerField(
        label = 'When you go outside on a sunny day for more than one hour, how likely aare you to use sunscreen or sunblock?',
        choices = [
            [1, 'Very likely'],
            [2, 'Somewhat likely'],
            [3, 'Unlikely']
            ],
        widget = widgets.RadioSelect
        )

    intelligent = models.IntegerField(
        label = "Compared to other people your age, how intelligent are you?",
        choices = [
            [1, 'Moderately below average'],
            [2, 'Slightly below average'],
            [3, 'About average'],
            [4, 'Slightly above average'],
            [5, 'Moderately above average'],
            [6, 'Extremely above average'],
            ],
        widget = widgets.RadioSelect
        )
    

    pray = models.IntegerField(
        label = "How often do you pray privately, that is, when you're alone in places other than a church, synagogue, temple, mosque, or religious assembly?",
        choices = [
            [0, 'Never'],
            [1, 'Less than once a month'],
            [2, 'Once a month'],
            [3, 'A few times a month'],
            [4, 'Once a week'],
            [5, 'A few times a week'],
            [6, 'Once a day'],
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


    dont_talk = models.IntegerField(
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
    expelled = models.BooleanField(
            label = 'Have you ever been expelled from school?',
            choices = [
                [True, 'Yes'],
                [False, 'No'],
                ],
            widget = widgets.RadioSelect
            )

    paid_sex = models.BooleanField(
            label = 'Have you ever paid someone to have sex with you or has someone paid you to have sex with them?',
            choices = [
                [True, 'Yes'],
                [False, 'No'],
                ],
            widget = widgets.RadioSelect
            )

    gambling = models.BooleanField(
            label = 'Have you ever bought lottery tickets, played video games or slot machines for money, bet on horses or sporting events, or taken part in any other kinds of gambling for money?',
            choices = [
                [True, 'Yes'],
                [False, 'No'],
                ],
            widget = widgets.RadioSelect
            )

    tobacco = models.BooleanField(
            label = 'Have you used chewing tobacco (such as Red Man, Garrett, or Beechnut) or snuff (such as Skoal, Skoal Bandits, or Copenhagen) at least 20 times in your entire life?',
            choices = [
                [True, 'Yes'],
                [False, 'No'],
                ],
            widget = widgets.RadioSelect
            )

    arrested = models.BooleanField(
            label = 'Have you ever been arrested?',
            choices = [
                [True, 'Yes'],
                [False, 'No'],
                ],
            widget = widgets.RadioSelect
            )

    military = models.BooleanField(
            label = 'Have you ever been in the military?',
            choices = [
                [True, 'Yes'],
                [False, 'No'],
                ],
            widget = widgets.RadioSelect
            )

     

    sun_hour = models.IntegerField(
            label = "During a typical summer week, how many hours do you spend in the sun during the day?",
            min=0,
            max=99
            )

    sweat = models.BooleanField(
            label = 'In the past 24h, have you participated in vigorous activity long enough to work up a sweat, get your heart thumping, or get out of breath?',
            choices = [
                [True, 'Yes'],
                [False, 'No'],
                ],
            widget = widgets.RadioSelect
            )






