"""
Implicit Association Test (IAT) experiment -- models.

Dynamic data points for IAT trials are collected in custom data model "Trial". See Konrad 2018 [1] for an article
on collection dynamic data with oTree using the package otreeutils [2].

[1] https://doi.org/10.1016/j.jbef.2018.10.006
[2] https://github.com/WZBSocialScienceCenter/otreeutils

November 2019
Markus Konrad <markus.konrad@wzb.eu>
"""

import random

# required for custom data models:
from otree.db.models import Model, ForeignKey

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Markus Konrad <markus.konrad@wzb.eu>'

doc = """
IAT – Implicit Association Test
"""

#
# configuration of stimuli: attribute and concept levels and stimuli words
# these are just made up stimuli; fill in your own
#

STIMULI = {
    'attributes': {
        'pos': ['pleasing','cheerful','magnificent','glorious','enjoy','friendship','joyous','laughing'],
        'neg': ['pain','sickening','annoy','disaster','sadness','evil','grief','bothersome']
    },
    'concepts': {
        'gay': ['gay people','homosexual','lesbians', 'img_gay', 'img_lesbian'],
        'straight': ['straight people','heterosexual','different sex','img_straight']
    }
}

STIMULI_LABELS = {
    ('attributes', 'pos'): 'Positive words',
    ('attributes', 'neg'): 'Negative words',
    ('concepts', 'gay'): 'Gay People',
    ('concepts', 'straight'): 'Straight People',
}

#
# configuration of practice and test blocks
#

BLOCKS = [
    {   # 1
        'label': 'Practice 1',
        'n': 9,      # this must match the number of stimuli per side
        'left': [('concepts', 'gay')],
        'right': [('concepts', 'straight')],
        'is_practice': True
    },
    {   # 2
        'label': 'Practice 2',
        'n': 16,
        'left': [('attributes', 'neg')],
        'right': [('attributes', 'pos')],
        'is_practice': True
    },
    {   # 3
        'label': 'Test 1',
        'n': 25,
        'left': [
            ('attributes', 'neg'),
            ('concepts', 'gay'),
        ],
        'right': [
            ('attributes', 'pos'),
            ('concepts', 'straight'),
        ]
    },
    {   # 4: same as #3
        'label': 'Test 2',
        'n': 25,
        'left': [
            ('attributes', 'neg'),
            ('concepts', 'gay'),
        ],
        'right': [
            ('attributes', 'pos'),
            ('concepts', 'straight'),
        ]
    },
    {   # 5
        'label': 'Practice 3 (reversed)',
        'n': 9,
        'left': [('concepts', 'straight')],
        'right': [('concepts', 'gay')],
        'is_practice': True,
        'notice': 'WATCH OUT, the categories switch sides!',
    },
    {  # 6
        'label': 'Test 3',
        'n': 25,
        'left': [
            ('attributes', 'neg'),
            ('concepts', 'straight'),
        ],
        'right': [
            ('attributes', 'pos'),
            ('concepts', 'gay'),
        ]
    },
    {  # 7: same as 6
        'label': 'Test 4',
        'n': 25,
        'left': [
            ('attributes', 'neg'),
            ('concepts', 'straight'),
        ],
        'right': [
            ('attributes', 'pos'),
            ('concepts', 'gay'),
        ]
    },
]


class Constants(BaseConstants):
    name_in_url = 'iat_so'
    players_per_group = None
    num_rounds = len(BLOCKS)                  # number of blocks to play
    capture_keycodes = {'left': ('KeyE', 'E'),
                        'right': ('KeyI', 'I')}
    next_trial_delay_ms = 250                 # delay between trials in millisec.


class Subsession(BaseSubsession):
    def creating_session(self):
        """
        Prepare trials for each round. Generates Trial objects.
        """

        # iterate through all players in all rounds
        trials = []
        for p in self.get_players():
            block_num = p.round_number - 1
            block_def = BLOCKS[block_num]    # get block definition for this round

            # create stimuli: class (attrib./concept) and level (e.g. pos./neg.) for left and right side
            stimuli = []
            for side in ('left', 'right'):
                for stim_class, stim_lvl in block_def[side]:
                    stim_vals = STIMULI[stim_class][stim_lvl]   # concrete stimuli words
                    n_vals = len(stim_vals)
                    stimuli.extend(zip([side] * n_vals, [stim_class] * n_vals, [stim_lvl] * n_vals, stim_vals))

            # randomize order
            random.shuffle(stimuli)

            if len(stimuli) != block_def['n']:
                raise ValueError('the number of stimuli (%d) and the number of repetitions in the block definition '
                                 '(n=%d) do not match' % (len(stimuli), block_def['n']))

            # generate Trial object for each stimulus
            for trial_i, stim_def in enumerate(stimuli):
                side, stim_class, stim_lvl, stim = stim_def

                trials.append(Trial(
                    block=p.round_number,
                    trial=trial_i+1,
                    stimulus=stim,
                    stimulus_class=stim_class,
                    stimulus_level=stim_lvl,
                    player=p
                ))

        Trial.objects.bulk_create(trials)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def response_record(self):
        #self.participant.vars[str(self.trial.block)+'_'+str(self.trial.trial)'_'+str(self.trial.stimulus)'_'+str(self.trial.stimulus_class)'_'+str(self.trial.stimulus_level)] = [self.trial.response_key,self.response_correct,self.response_time_ms]
        self.participant.vars[str(self.trial.block)] = self.response_time_ms

class Trial(Model):
    """
    Trial model holds all information for a single trial made by a player.
    This is a "custom data model" in a 1:n relationship between Player and Trial.
    It uses an otreeutils "CustomModelConf" for monitoring and exporting the collected data from this model.
    """
    block = models.IntegerField()  # block number (-> round number)
    trial = models.IntegerField()  # trial number in that round for that participant

    stimulus = models.StringField()          # shown word or name
    stimulus_class = models.StringField()    # words or names
    stimulus_level = models.StringField()    # pos/neg or tr/dt

    response_key = models.StringField()       # response: key that was pressed by participant
    response_correct = models.BooleanField()  # records whether response was correct
    response_time_ms = models.IntegerField()  # time it took until key was pressed since word/name was shown

    player = ForeignKey(Player,on_delete=models.StringField())               # make a 1:n relationship between Player and Trial

    class CustomModelConf:
        """
        Configuration for otreeutils admin extensions.
        """
        data_view = {  # define this attribute if you want to include this model in the live data view
            'exclude_fields': ['player'],
            'link_with': 'player'
        }
        export_data = {  # define this attribute if you want to include this model in the data export
            'exclude_fields': ['player_id'],
            'link_with': 'player'
        }
