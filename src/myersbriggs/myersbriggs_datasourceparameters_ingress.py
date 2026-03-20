"""Created on 20260311"""
class MyersBriggsDataSourceParametersIngress:
    """
    The class contains general parameters that facilitate the data ingress between 
    data sources and MyersBriggs* related objects. 
    """
    def __init__(self, id : str, name : str):
        """
        The identifier for the MyersBriggsDataSourceParametersIngress object.
        The name for this object.
        """
        self.id = id
        self.name = name