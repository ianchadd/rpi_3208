from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'player'
    form_fields = ['kept']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    def vars_for_template(self):
        return dict(offer=Constants.endowment - self.player.kept)


page_sequence = [Introduction, Offer, ResultsWaitPage, Results]
