"""Created on 20260311_1630"""
import uuid

class MyersBriggsUniverse:
    """
    The MyersBriggsUniverse should "contain" all the other MyersBriggs* objects.
    """
    def __init__(self, name : str):
        """
        The name for the MyersBriggsUniverse object.
        The universeid holds this object's guid. 
        """
        self.name = name
        self.universeid = uuid.uuid4()

    def __str__(self):
        return f"Universe '{self.name}' has guid '{self.universeid}'"
    
    def __repr__(self):
        return f"Universe '{self.name}' has guid '{self.universeid}'"
    
    @staticmethod
    def __main_demo__():
        """
        This function demonstrates how to intiailization of the following objects:
        MyersBriggsUniverse
        """
        mbu = MyersBriggsUniverse('George Romero Zombie Universe')
        print(mbu)

if __name__ == "__main__":
    MyersBriggsUniverse.__main_demo__()