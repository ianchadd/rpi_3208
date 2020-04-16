from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Request_Screen(Page):
    form_model = 'player'
    form_fields = ['volunteer']


class Results_Wait_Page(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    body_text = "Waiting for other participants to finish."

class Role_Announcement(page):
    #do the randomly assigned investor thing
    form_model = 'player'
    form_fileds = ['volunteer']

class Role_Wait_Page(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    body_text = "Waiting for other participants to finish."

class Investment_Decisions(page):
    timeout_seconds = 60
    form_model = 'player'
    form_fields = ['volunteer']

class Results(Page):
    pass


page_sequence = [Introduction, Request_Screen, Results_Wait_Page, Role_Announcement, Role_Wait_Page, Investment_Decisions, Results]
