"""Created on 20260311"""
class MyersBriggsDataSourceParametersEgress:
    """
    The class contains general parameters that facilitate the data egress between 
    MyersBriggs* related objects and data sources.
    """
    def __init__(self, id : str, name : str):
        """
        The identifier for the MyersBriggsDataSourceParametersEgress object.
        The name for this object.
        """
        self.id = id
        self.name = name