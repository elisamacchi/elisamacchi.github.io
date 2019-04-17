from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    pass


class Income(Page):
    form_model = 'player'
    form_fields = ['q1_1']

    def vars_for_template(self):
        return {
            'image_path': 'experiment_1/{}.jpg'.format(self.round_number)
        }


class Health(Page):
    form_model = 'player'
    form_fields = ['q2_1']

    def vars_for_template(self):
        return {
            'image_path': 'experiment_1/{}.jpg'.format(self.round_number)
        }


class Attractiveness(Page):
    form_model = 'player'
    form_fields = ['q3_1']

    def vars_for_template(self):
        return {
            'image_path': 'experiment_1/{}.jpg'.format(self.round_number)
        }


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'partnerincome', 'bodymass', 'idealbodymass', 'height', 'weight', 'cob']


class Issues(Page):
    form_model = 'player'
    form_fields = ['issues']


class Comments(Page):
    form_model = 'player'
    form_fields = ['comments']


page_sequence = [
    Instructions,
    Income,
    Health,
    Attractiveness,
    Demographics,
    Issues,
    Comments
]
