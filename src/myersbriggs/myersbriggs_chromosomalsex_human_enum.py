"""Created on 20260311_1300"""
from enum import Enum, unique
from myersbriggs.utils.myersbriggs_util import MyersBriggsUtil

@unique
class MyersBriggsChromosomalSexHumanEnum(Enum):
    """
    The creation of clinical chromosomal sex categories.
    The values were not represented as numbers to avoid simple modifications.
    The values are the results of the sha-1 hash function.
    """
    XX      = '20026dc165c030fe3a5d9609a6e61ab26210cbc1'
    XY      = '034f1965ccdbdf9e642feeb9858da5096b6d1a9a'
    XO      = '8acc5a4d5064b1a7ad7e1842e0711814022a140d'
    XXY     = '5062442656eb3a05fde4a9322664a913c88be109'
    XYY     = 'f5c5be6b78de5f758481aa2af73bf705e232ea09'
    XXX     = 'a9674b19f8c56f785c91a555d0a144522bb318e6'