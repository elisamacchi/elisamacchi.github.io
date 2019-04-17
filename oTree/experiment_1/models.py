from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Elisa Macchi'

doc = """ Experiment 1 : Test how body mass affects perceived income """


class Constants(BaseConstants):
    name_in_url = 'experiment_1'
    players_per_group = None
    num_rounds = 1
    pilot = 'yes'
    payoff = 1
    imgs = [""]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Pictures:

    q1_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # income
    q2_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # health
    q3_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # attractiveness

    # Understanding Question:

    uq_1 = models.IntegerField()
    uq_2 = models.IntegerField()
    uq_3 = models.IntegerField()

    # Rankings:

    # BMI
    r1_1 = models.IntegerField()
    r1_2 = models.IntegerField()
    r1_3 = models.IntegerField()


    # Demographics:

    age = models.IntegerField(min=18, max=99)
    gender = models.IntegerField(choices=[1, 2])
    income = models.IntegerField()
    partnerincome = models.IntegerField(blank=True)
    bodymass = models.IntegerField()
    idealbodymass = models.IntegerField()
    height = models.IntegerField(min=150, max=200)
    weight = models.IntegerField(min=40, max=300)
    cob = models.StringField()

    # Check:

    issues = models.LongStringField()
    comments = models.LongStringField()








