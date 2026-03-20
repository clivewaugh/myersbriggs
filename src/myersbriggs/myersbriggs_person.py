"""Created on 20260311"""
from myersbriggs.myersbriggs_personality_entity import MyersBriggsPersonalityEntity
from myersbriggs.myersbriggs_personality_enum import MyersBriggsPersonalityEnum 
from myersbriggs.myersbriggs_chromosomalsex_human_enum import MyersBriggsChromosomalSexHumanEnum

class MyersBriggsPerson(MyersBriggsPersonalityEntity):
    """
    The MyersBriggsPerson is the MyersBriggsPersonalityEntity that 
    added the chromosomal sex type.
    MyersBriggsPerson is the foundation class that encapsulates MBTI characteristics. 
    """
    def __init__(self, name : str, personalitytype : MyersBriggsPersonalityEnum, chromosomesex : MyersBriggsChromosomalSexHumanEnum):
        """
        The name of the MyersBriggsPersonalityEntity object.
        The personalitytype holds the MBTI characteristic.
        The chromosomesex holds the chromosomal sex type.
        """
        super().__init__(name, personalitytype)
        self.chromosomesex = chromosomesex

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Person '{self.name}' has personality '{self.personalitytype}' and chromosome '{self.chromosomesex}'"

    def main(self):
        return
    
    @staticmethod
    def __main_demo__():
        """
        This function demonstrates how to intiailize and use the following objects:
        MyersBriggsPerson
        """
        instance = MyersBriggsPerson('Code Bro2', MyersBriggsPersonalityEnum.ENFJ.name, MyersBriggsChromosomalSexHumanEnum.XO._name_)
        print(instance.__repr__())

if __name__ == "__main__":
    MyersBriggsPerson.__main_demo__()




