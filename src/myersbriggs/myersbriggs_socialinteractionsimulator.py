"""Created on 20260312"""
from myersbriggs.myersbriggs_socialinteractionsurface_hexagon import MyersBriggsSocialInteractionSurfaceHexagon
from myersbriggs.myersbriggs_person import MyersBriggsPerson
from myersbriggs.myersbriggs_personality_enum import MyersBriggsPersonalityEnum 
from myersbriggs.myersbriggs_chromosomalsex_human_enum import MyersBriggsChromosomalSexHumanEnum
from myersbriggs.utils.myersbriggs_util import MyersBriggsUtil

class MyersBriggsSocialInteractionSimulator:
    """The class simulates the communications and actions between entities."""
    def __init__(self, id : str, name: str, version : str):
        """The id is the identifier for the simulator. The name is similar to a description. The version clarifies the name"""
        self.id = id
        self.name = name
        self.version = version

    def sim(self, social_interaction_surface : MyersBriggsSocialInteractionSurfaceHexagon):
        """The MyersBriggsSocialInteractionSurfaceHexagon holds the players around a single person"""
        return self.__sim_demo(social_interaction_surface)
    
    def __sim_demo(self, social_interaction_surface : MyersBriggsSocialInteractionSurfaceHexagon):
        """
        The function is demo version of the output from the MyersBriggsSocialInteractionSurfaceHexagon.
        In future implementations this function will return results from other APIs that create or simulate interactions between various persons.
        The AI agents will take the the MBTI and chromosonal sex with a scenario object to create communications and actions.
        """
        if social_interaction_surface.checkValid() == False:
            return f"{MyersBriggsSocialInteractionSimulator.sim.__qualname__} exited prematurely"
        
        narration   = ''
        narration   += f"{self.__repr__()}\n" 
        narration   += f"They following takes place in '{social_interaction_surface.desc}'.\n"
        narration   += f"Our character '{social_interaction_surface.focus}' is with "

        if len(social_interaction_surface.friends) > 0:
            for friend in social_interaction_surface.friends[:-1]:
                mbp_friend  = social_interaction_surface.cast_a_friend_to_type(friend)
                narration   += f"'{mbp_friend.name}', "    
            for friend in social_interaction_surface.friends[-1:]:
                mbp_friend  = social_interaction_surface.cast_a_friend_to_type(friend)
                narration   += f"'{mbp_friend.name}'"

        narration   += f".\nThey are surrounded by "
   
        if len(social_interaction_surface.foes) > 0:
            for foe in social_interaction_surface.foes[:-1]:
                mbp_foe     = social_interaction_surface.cast_a_foe_to_type(foe)
                narration   += f"'{mbp_foe.name}', "
            for foe in social_interaction_surface.foes[-1:]:
                mbp_foe     = social_interaction_surface.cast_a_foe_to_type(foe)
                narration   += f"'{mbp_foe.name}'"
        
        narration   += f".\nWhile onlookers "

        if len(social_interaction_surface.fences) > 0:
            for fence in social_interaction_surface.fences[:-1]:
                mbp_fence   = social_interaction_surface.cast_a_fence_to_type(fence)
                narration   += f"'{mbp_fence.name}', "
            for fence in social_interaction_surface.fences[-1:]:
                mbp_fence   = social_interaction_surface.cast_a_fence_to_type(fence)
                narration   += f"'{mbp_fence.name}'"
        
        narration   += f" stay out the way.\n"

        return narration
    
    def __str__(self):
        return f"Simulator id '{self.id}' is titled '{self.name}' of version '{self.version}'"
    
    def __repr__(self):
        return f"Simulator id '{self.id}' is titled '{self.name}' of version '{self.version}'"
    
    def main(self):
        return
    
    @staticmethod
    def __main_demo__():
        """
        This function demonstrates how to intiailize and use the following objects:
        MyersBriggsPerson
        MyersBriggsSocialInteractionSurfaceHexagon
        MyersBriggsSocialInteractionSimulator
        """
        mbp_focus   = MyersBriggsPerson('Sonny', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_friend1 = MyersBriggsPerson('Calogero', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_friend2 = MyersBriggsPerson('Jimmy Whispers', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_friend3 = MyersBriggsPerson('JoJo the Whale', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_foe1    = MyersBriggsPerson('Satans Messenger 1', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_foe2    = MyersBriggsPerson('Satans Messenger 2', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_foe3    = MyersBriggsPerson('Satans Messenger 3', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_foe4    = MyersBriggsPerson('Satans Messenger 4', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_foe5    = MyersBriggsPerson('Satans Messenger 5', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_foe6    = MyersBriggsPerson('Satans Messenger 6', MyersBriggsPersonalityEnum.ENFJ, MyersBriggsChromosomalSexHumanEnum.XY)
        mbp_fence1  = MyersBriggsPerson('Bartender 1', MyersBriggsPersonalityEnum.ISTP, MyersBriggsChromosomalSexHumanEnum.XY)

        list_friend = []
        list_friend.append(mbp_friend1)
        list_friend.append(mbp_friend2)
        list_friend.append(mbp_friend3)

        list_foe    = []
        list_foe.append(mbp_foe1)
        list_foe.append(mbp_foe2)
        list_foe.append(mbp_foe3)
        list_foe.append(mbp_foe4)
        list_foe.append(mbp_foe5)
        list_foe.append(mbp_foe6)

        list_fence = []
        list_fence.append(mbp_fence1)

        mysish      = MyersBriggsSocialInteractionSurfaceHexagon('0001', 'Bronx Bar Brawl', mbp_focus, list_friend, list_foe, list_fence)
        instance    = MyersBriggsSocialInteractionSimulator('0001', 'A Bronx Tale: Now youse cant leave', 'v.001')
        sim_output = instance.sim(mysish)
        print(sim_output)
        

if __name__ == "__main__":
    MyersBriggsSocialInteractionSimulator.__main_demo__()