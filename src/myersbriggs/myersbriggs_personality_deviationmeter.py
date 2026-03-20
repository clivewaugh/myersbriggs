"""Created on 20260311_2145"""
from myersbriggs.myersbriggs_person import MyersBriggsPerson

class MyersBriggsPersonalityDeviationMeter:
    """
    The MyersBriggsPersonalityDeviationMeter is an experimental meter of 
    termporary changes to a person's MTBI characteristic and behavior. 
    """
    def __init__(self, focus : MyersBriggsPerson):
        """
        The focus person.
        """
        self.focus = focus 
        