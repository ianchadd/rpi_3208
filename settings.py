from os import environ
import json

if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
    APPS_DEBUG = False
else:
    DEBUG = True
    APPS_DEBUG = True   # also enables random fill in of forms


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
    round_values = ["1.00"],
    piece_rate = 0.25,
    seconds_for_counting_task=5,
    guess_rate = 0.20,
    delay = False,
    consent_link = False,
    consent_url = 'xxxxx'
)


SESSION_CONFIGS = [
    dict(name='iat', display_name="IAT", num_demo_participants=2, app_sequence=['iat_so']),
    dict(
        name='qsp_recip',
        display_name="QSP Recipient",
        num_demo_participants=3,
        app_sequence=[
                        'prolific_ID_begin',
                        'informed_consent',
                        'qsp_dg_recip_intro',
                        'qsp_dg_recip_id',
                        'dg_recip_survey',
                        'qsp_dg_recip_id_2',
                        'dg_recip_survey_p2',
                        'survey_demographics_qsp',
                        'feedback_survey',
                        'prolific_ID_end'
                        ],
        participation_fee = 2.00,
        recip = True,
        delay = True,
        consent = 'flag_survey/consent.pdf',
        consent_url = 'https://virtual-experimental-lab.github.io/virtual-experimental-lab.github.io/1932%20IRB%20Approved%20Consent%20Form%208%2018%2020.pdf',
        consent_link = True,
        p_completion_link = 'xxxxxxxx',
    ),
    dict(
        name='qsp_dictator',
        display_name="QSP Dictator",
        num_demo_participants=1,
        pw = 'qsp_testing',
        app_sequence=[
                    'prolific_ID_begin',
                    'informed_consent',
                    'qsp_dg_dict_intro',
                      'qsp_dg_dict_instructions',
                      'dg_qsp',
                      'dg_qsp_survey',
                      'survey_demographics_qsp',
                        'iat_so',
                    'feedback_survey',
                    'prolific_ID_end'
                      ],
        participation_fee = 2.00,
        recip=False,
        delay = True,
        consent = 'flag_survey/consent.pdf',
        consent_url = 'https://virtual-experimental-lab.github.io/virtual-experimental-lab.github.io/1932%20IRB%20Approved%20Consent%20Form%208%2018%2020.pdf',
        consent_link = True,
        p_completion_link = 'xxxxxxxx',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """
    ),
    dict(
        name='gt_survey_test',
        display_name="Gender Typicality",
        num_demo_participants=3,
        app_sequence=['testing_pw',
                      'gender_typicality'],
        participation_fee = 0,
        p_completion_link = 'xxxxxxxx',
        pw = 'gt_testing',
        questions = [
                     'arrested',
                     'intelligent',
                     'imagination',
                     'military',
                     'mood',
                     'others_problems',
                     'others_interested',
                     'pray',
                     'risks',
                     'stress',
                     'sun',
                     'sunblock',
                     'strength',
                     'sweat',
                     'team_sports',
                     'tired',
                     'walk',
                     'sympathize',
                     'talk',
                     'tobacco',
                     'video_games',
                     'worry'
                     ],
        random = True,
        survey_title = 'GT Survey',
        doc="""
    Edit the p_completion_link variable with the completion code for Prolific session
    """

    ),
    dict(
        name='cw',
        display_name="CW",
        num_demo_participants=3,
        app_sequence=['testing_pw',
                      'cw_instructions',
                      'cw_practice'
                      ],
        participation_fee = 2.00,
        p_completion_link = 'xxxxxxxx',
        pw = 'cw_testing'
    ),
    dict(
        name='QCP',
        num_demo_participants=1,
        #use_browser_bots=True,
        app_sequence=[
            'prolific_ID_begin',
            'informed_consent',
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
            'qcp_demographics',
            #'Survey',
            #'feedback_survey',
            'gender_typicality',
            'Summary',
            'feedback_survey_qcp',
            'prolific_ID_end'],
            consent = 'qcp/consent.pdf',
        p_completion_link = 'xxxxxxxx',
        consent_additional_message = """
        """,
        consent_url = 'https://billuraksoy.github.io/virtual_lab/consent_form_2022.pdf',
        consent_link = True,
        seed_data = False,
        data_pages_enabled=False,
        summary_page_enabled=True,
        participation_fee=2.00,
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
        participation_fee = 1.00,
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
        app_sequence=['prolific_ID_begin',
                        'informed_consent',
                      'NBO_choice',
                      'survey_demographics_nbo',
                      'prolific_ID_end',],
        treat = 'baseline',
        participation_fee = 1.00,
        real_world_currency_per_point = 0.10,
        consent = 'no_choice/consent.pdf',
        p_completion_link = 'xxxxxxxx',
        consent_additional_message = """
        Please note that the form above is used for several experiments.
        In this experiment we expect that you will make at least $2.25 plus a bonus payment based on your decisions.
        """,
    ),
    dict(
        name='nbo_choice_nbo',
        num_demo_participants=3,
        app_sequence=['prolific_ID_begin',
                        'informed_consent',
                      'NBO_choice',
                      'survey_demographics_nbo',
                      'prolific_ID_end',],
        treat = 'nbo',
        real_world_currency_per_point = 0.10,
        participation_fee = 1.00,
        consent = 'no_choice/consent.pdf',
        p_completion_link = 'xxxxxxxx',
        consent_additional_message = """
        Please note that the form above is used for several experiments.
        In this experiment we expect that you will make at least $2.25 plus a bonus payment based on your decisions.
        """,
    ),
    dict(
        name='nbo_choice_exo',
        num_demo_participants=2,
        app_sequence=['prolific_ID_begin',
                        'informed_consent',
                      'NBO_choice',
                      'survey_demographics_nbo',
                      'prolific_ID_end',],
        treat = 'exo',
        real_world_currency_per_point = 0.10,
        participation_fee = 1.00,
        consent = 'no_choice/consent.pdf',
        p_completion_link = 'https://app.prolific.co/submissions/complete?cc=2C0A1220',
        consent_additional_message = """
        Please note that the form above is used for several experiments.
        In this experiment we expect that you will make at least $2.25 plus a bonus payment based on your decisions.
        """,
    ),
    dict(
        name = 'faces',
        display_name = 'Faces Barebones Code',
        num_demo_participants =  1,
        app_sequence = [
            #'testing_pw',
            #'icl',
            'image_upload',
            #'survey_faces'
            ],
        pw = 'faces_testing',
        participation_fee = 1.00,
        consent = '',
        p_completion_link = 'xxxxxxxx',
        doc=    """
                """
    ),
    dict(
       name='slider_puzzle',
       display_name="Slider Puzzle - Two Player real time variant w/ move tracking",
       num_demo_participants=4,
       app_sequence=['slider_puzzle']
    ),
    dict(
        name='single_player_puzzle',
        display_name="Slider Puzzle - Single Player variant w/o move tracking",
        num_demo_participants=2,
        app_sequence=['single_player_puzzle']
    ),
    dict(
        name='main_session',
        display_name='Full session',
        num_demo_participants=24,
        app_sequence=['pt0', 'pt1', 'pt1grp', 'pt2', 'pt2grp',
                      'pt3', 'pt4', 'pt99'],
        test=0,
        participation_fee=0,  # this is set to 0 b/c this is added to payoff
        real_world_currency_per_point=1,
        partfee=2,
        pt1rate=0.2,
        pt3rate=1,
        num_part=16,
        max_earning=25,
        uq_error='Controlla la tua risposta.',
        doc="""
        Program for gender differences in the cost of contradictions.
        Number of participants: multiple of 8.
        Max number of participants: 32 (can be larger, but need to modify codes)
        """
    ),
    dict(
        name='main_session_test',
        display_name='Full session (Shorter version)',
        num_demo_participants=24,
        app_sequence=['pt0', 'pt1', 'pt1grp', 'pt2', 'pt2grp',
                      'pt3', 'pt4', 'pt99'],
        test=1,
        participation_fee=0,  # this is set to 0 b/c this is added to payoff
        real_world_currency_per_point=1,
        partfee=2,
        pt1rate=0.2,
        pt3rate=1,
        num_part=16,
        max_earning=25,
        uq_error='Controlla la tua risposta.',
        doc="""
        Program for gender differences in the cost of contradictions.
        Number of participants: multiple of 8.
        Max number of participants: 32 (can be larger, but need to modify codes)
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
    dict(
        name='rpi_lab_qsp_1',
        display_name='RPI Virtual Econ Laboratory: QSP 1'
    ),
    dict(
        name='rpi_lab_qsp_2',
        display_name='RPI Virtual Econ Laboratory: QSP 2'
    ),
    dict(
        name='rpi_lab_qsp_3',
        display_name='RPI Virtual Econ Laboratory: QSP 3'
    ),
    dict(
        name='rpi_lab_qsp_4',
        display_name='RPI Virtual Econ Laboratory: QSP 4'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""
# extra settings for otreeutils
# ROOT_URLCONF = 'iat_so.urls'
# CHANNEL_ROUTING = 'iat_so.routing.channel_routing'
# don't share this with anybody.
SECRET_KEY = '7vfsh(zo@d)v)zizkf#@xqzb3q%juzu65zoh4r+#$tckdfji5r'

INSTALLED_APPS = ['otree',
                  'custom_templates',
                  'django.contrib.humanize',
                  'otreeutils'
                  ]
EXTENSION_APPS = ['slider_puzzle']
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
