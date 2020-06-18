from os import environ
import json

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
sample_participants = []
with open('sample_participants.json') as sample_participants:
    sample_participants=json.load(sample_participants)
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.50, doc="",
    data_pages_enabled=True,
    sample_participants=sample_participants,
    num_sample_participants=10,
    consent_additional_message = """""",
    round_values = ["0.25", "0.50","0.75","1.00","1.25","1.50","1.75"],
    piece_rate = 0.25,
    seconds_for_counting_task=10,
    guess_rate = 0.20
)


SESSION_CONFIGS = [
    dict(
        name='Simple_survey_flag',
        display_name="QSP Survey 1",
        num_demo_participants=3,
        app_sequence=['prolific_ID_begin',
                      'simple_survey_flag',
                      'survey_demographics',
                      'prolific_ID_end'],
        participation_fee = 2.00,
        p_completion_link = 'xxxxxxxx',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """
        
    ),
    dict(
        name='QCP',
        num_demo_participants=1,
        #use_browser_bots=True,
        app_sequence=[
            'Introduction',
            'Introduction_Practice',
            'Game_1',
            'Game_1_Game',
            'Game_1_Data',
            'Game_2',
            'Game_2_Game',
            'Game_2_Data',
            'Game_3',
            'Game_3_Game',
            'Game_3_Data',
            'Game_4',
            'Game_4_Data',
            #'Game_5',
            #'Game_5_Game',
            #'Game_5_Data',
            'Performance_Guesses',
            #'Survey',
            'Summary']
    ),
    dict(
        name='demo_survey',
        display_name="Demographic Survey",
        num_demo_participants=3,
        app_sequence=['survey_demographics']
    ),
    dict(
        name='demo_survey_2',
        display_name="Demographic Survey 2",
        num_demo_participants=3,
        app_sequence=['survey_demographics']
    ),
    dict(
        name='volunteer',
        display_name="Volunteer Dilemma",
        num_demo_participants=3,
        app_sequence=['volunteer_dilemma']
    ),
    dict(
        name='nbo_choice',
        num_demo_participants=3,
        app_sequence=['prolific_ID_begin',
                      'informed_consent',
                      'NBO_choice',
                      'survey_demographics_nbo',
                      'prolific_ID_end',],
        real_world_currency_per_point = 0.10,
        consent = 'no_choice/consent.pdf',
        p_completion_link = 'xxxxxxxx',
        consent_additional_message = """
        Please note that the form above is used for several experiments.
        In this experiment we expect that you will make at least $2.25 plus a bonus payment based on your decisions.
        """,
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """ 
    ),
    dict(
        name='nbo_choice_baseline',
        num_demo_participants=3,
        app_sequence=['informed_consent',
                      'NBO_choice',
                      'survey_demographics_nbo'],
        treat = 'baseline',
        real_world_currency_per_point = 0.10,
        consent = 'no_choice/consent.pdf'
    ),
    dict(
        name='nbo_choice_nbo',
        num_demo_participants=3,
        app_sequence=['informed_consent',
                      'NBO_choice',
                      'survey_demographics_nbo'],
        treat = 'nbo',
        real_world_currency_per_point = 0.10,
        consent = 'no_choice/consent.pdf'
    ),
    dict(
        name='id_dg',
        display_name="QSP ID + DG (Testing)",
        num_demo_participants=1,
        app_sequence=['prolific_ID_begin',
                      'simple_survey_flag',
                      'dg_qsp',
                      'prolific_ID_end'],
        participation_fee = 2.00,
        p_completion_link = 'xxxxxxxx',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """  
    ),
    dict(
        name='id_pd',
        display_name="QSP ID + PD (Testing)",
        num_demo_participants=1,
        app_sequence=[#'prolific_ID_begin',
                      'simple_survey_flag',
                      'pd_qsp',
                      #'prolific_ID_end'
                      ],
        participation_fee = 2.00,
        p_completion_link = 'xxxxxxxx',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """  
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(name='prolific_qsp', display_name='Prolific Room for QSP (no participant labels)'),
    dict(
        name='rpi_lab',
        display_name='RPI Virtual Econ Laboratory'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '7vfsh(zo@d)v)zizkf#@xqzb3q%juzu65zoh4r+#$tckdfji5r'

INSTALLED_APPS = ['otree','custom_templates']

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
