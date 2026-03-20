"""Created on 20260311"""
from myersbriggs.myersbriggs_personality_enum import MyersBriggsPersonalityEnum

class MyersBriggsPersonalityEntity:
    """
    The MyersBriggsPersonalityEntity is the base class for all MyersBriggsPersonalityEntity subclasses  
    that will have MBTI characteristics.
    """
    def __init__(self, name : str, personalitytype : MyersBriggsPersonalityEnum):
        """
        The name of the MyersBriggsPersonalityEntity object.
        The personalitytype holds the MBTI characteristic.
        """
        self.name = name
        self.personalitytype = personalitytype

    def __str__(self):
        return f"MyersBriggsPersonalityEntity '{self.name}' has personality '{self.personalitytype}'"
    
    def __repr__(self):
        return f"MyersBriggsPersonalityEntity '{self.name}' has personality '{self.personalitytype}'"