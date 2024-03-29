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


doc = """
Panas-x-scale
"""


class Constants(BaseConstants):
    name_in_url = 'emotions_video_instructions'
    players_per_group = None
    num_rounds = 1
    Contactenos = 'emotions_video_instructions/Contactenos.html'

class Subsession(BaseSubsession):
    pass    

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

