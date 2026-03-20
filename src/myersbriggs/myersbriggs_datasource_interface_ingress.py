"""Created on 20260311_2045"""
from abc import ABC, abstractmethod
from myersbriggs.myersbriggs_datasourceparameters_ingress import MyersBriggsDataSourceParametersIngress

class MyersBriggsDataSourceInterfaceIngress(ABC):
    """
    The interface that allows subclasses to facilitate data ingress.
    """
    @abstractmethod
    def ingress(self, datasource_params_ingress : MyersBriggsDataSourceParametersIngress):
        """
        The MyersBriggsDataSourceParametersIngress object.
        """
        self.datasource_params_ingress = datasource_params_ingress