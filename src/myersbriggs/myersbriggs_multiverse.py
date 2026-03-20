"""Created on 20260311_1630"""
from myersbriggs.myersbriggs_universe import MyersBriggsUniverse

class MyersBriggsMultiverse(MyersBriggsUniverse):
    """
    The MyersBriggsMultiverse should "contain" all the other MyersBriggs* objects.
    """
    def __init__(self, name):
        """
        The name for the MyersBriggsMultiverse object.
        """
        super().__init__(name)

    def __str__(self):
        return f"Multiverse '{self.name}' has guid '{self.universeid}'"
    
    def __repr__(self):
        return f"Multiverse '{self.name}' has guid '{self.universeid}'"

    @staticmethod
    def __main_demo__():
        """
        This function demonstrates how to intiailize and call the following objects:
        MyersBriggsMultiverse
        """
        mbm = MyersBriggsMultiverse('Marvel Cinematic Universe')
        print(mbm)

if __name__ == "__main__":
    MyersBriggsMultiverse.__main_demo__()

