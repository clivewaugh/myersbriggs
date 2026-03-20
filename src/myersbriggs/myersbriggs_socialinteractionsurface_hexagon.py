"""Created on 20260311_2145"""
from myersbriggs.myersbriggs_person import MyersBriggsPerson
from myersbriggs.utils.myersbriggs_util import MyersBriggsUtil
from typing import cast

class MyersBriggsSocialInteractionSurfaceHexagon:
    """
    The class holds the simplest connective associations to a single MBTI person, the focus.
    The friends are persons who are allies of the focus.
    The foes are persons who are antagonists of the focus.
    The fences are persons who are neutral with regards to their relationship to the focus.
    The fences are the similar Swiss, who are geopolitcally neutral among conflicts.
    Other classes may be created similar to the hexagon concept, 
    which model more complex internodal structures.   
    """
    def __init__(self, id : str, desc : str, focus : MyersBriggsPerson, friends : list, foes : list, fences : list):
        """
        The identifier for the MyersBriggsSocialInteractionSurfaceHexagon object.
        The description of this object.
        The focus object is the MyersBriggsPerson who that drives the social interaction.
        The friends list holds the MyersBriggsPerson whom are allies of the focus.
        The foes list holds the MyersBriggsPerson whom that are antagonists of the focus.
        The fences list holds the MyersBriggsPerson whom that are neutral towards the focus.
        """
        self.id = id
        self.desc = desc
        self.focus = focus
        self.friends = friends
        self.foes = foes
        self.fences = fences

    def checkValid(self) -> bool:
        """The function checks the data and object integrity of the members of the MyersBriggsSocialInteractionSurfaceHexagon"""
        error_msgs = []

        if MyersBriggsUtil.isListSameType(self.friends, MyersBriggsPerson) == False:
            error_msgs.append(f"Incorrect object types in {MyersBriggsPerson.__name__}.friends {type(self.friends)}. Expected {MyersBriggsPerson.__name__}")
        if MyersBriggsUtil.isListSameType(self.foes, MyersBriggsPerson) == False:
            error_msgs.append(f"Incorrect object types in {MyersBriggsPerson.__name__}.foes {type(self.foes)}. Expected {MyersBriggsPerson.__name__}")
        if MyersBriggsUtil.isListSameType(self.fences, MyersBriggsPerson) == False:
            error_msgs.append(f"Incorrect object types in {MyersBriggsPerson.__name__}.fences {type(self.fences)}. Expected {MyersBriggsPerson.__name__}")
       
        if len(error_msgs) > 0:
            print('\n'.join(error_msgs))
            return False
        
        return True
    
    def cast_a_friend_to_type(self, somefriend : any) -> MyersBriggsPerson:
        """
        The function performs a cast conversion of the input parameter into the MyersBriggsPerson type.
        It is intended to be used while looping over elements of the MyersBriggsSocialInteractionSurfaceHexagon.friends list.
        """
        return cast(MyersBriggsPerson, somefriend)
    
    def cast_a_foe_to_type(self, somefoe : any) -> MyersBriggsPerson:
        """
        The function performs a cast conversion of the input parameter into the MyersBriggsPerson type.
        It is intended to be used while looping over elements of the MyersBriggsSocialInteractionSurfaceHexagon.foes list.
        """
        return cast(MyersBriggsPerson, somefoe)
    
    def cast_a_fence_to_type(self, somefence : any) -> MyersBriggsPerson:
        """
        The function performs a cast conversion of the input parameter into the MyersBriggsPerson type.
        It is intended to be used while looping over elements of the MyersBriggsSocialInteractionSurfaceHexagon.fences list.
        """
        return cast(MyersBriggsPerson, somefence)
