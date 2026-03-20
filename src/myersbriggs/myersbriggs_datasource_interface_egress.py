"""Created on 20260311_2045"""
from abc import ABC, abstractmethod
from myersbriggs.myersbriggs_datasourceparameters_egress import MyersBriggsDataSourceParametersEgress

class MyersBriggsDataSourceInterfaceEgress(ABC):
    """
    The interface that allows subclasses to facilitate data egress.
    """
    @abstractmethod
    def egress(self, datasource_params_egress : MyersBriggsDataSourceParametersEgress):
        """
        The MyersBriggsDataSourceParametersEgress object.
        """
        self.datasource_params_egress = datasource_params_egress
