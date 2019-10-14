# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:50:15 2019

@author: yhossam

This module should be added to any package before registering it in the framework. 
It should contain all the necassary classes for the auto-training frame work to work properly.

"""
from autotraining.model import *
import pandas as pd
from typing import Iterable,Dict,Union,List,Tuple
from enum import Enum


#NOTE: You should run this module after adding your code to make sure it doesn't have any compilation errors.


"""    
NOTE: all methods marked with the comment '#TODO: OPTIONAL METHOD' just before their definition are optional.
An optional function is one that is already implemented in the base class so if you didn't implement it, the base class method will be used instead.
The base class method behaviour (default behaviour) is described in each method's summary.
"""



class MyModelsEvaluator(ModelsEvaluator):
    
    
    #TODO: OPTIONAL METHOD 
    def evalModels(self,modelsResults:Dict[str,ModelEvalOutput])->ModelsEvaluationResult:
        """
        Evaluates all models based on the output of each model's trainEvalModel function. Default  behaviour is to only save models that returned true from its trainEval function.
        Args:   
            modelsResults (Dict[str,ModelEvalOutput]): dictionary with pairs {modelClassName:object representing the model evaluation output.}
        Returns:
            ModelsEvaluationResult: Returns the result of the models evaluation using Enum class ModelsEvaluationResult. 
            The available options are: Save all new models, Save models with true evaluation only, ignore all models.
            Check the enum class ModelsEvaluationResult in the model.py module for more details
            to .
        """



class MyDataManager(DataManager):
    """ A class for data related methods such as extraction,preprocessing and sampling. A subclass of this class that overrides all the abstract methods must be included in any package added to the framework.
    """
    

    #TODO: OPTIONAL METHOD
    def sampleRawData(self,rawData:Iterable[pd.DataFrame])->Iterable[pd.DataFrame]:
        """Samples the raw data, so that the mock run carried out during the installation of the package is executed on a small subset of the data.
        
        Args:
            rawData (Iterable[pd.DataFrame]): Data frames containing raw data.
        
        Returns:
            Iterable[pd.DataFrame]: Data frames containing a subset of raw data that will be used in the mock run.
        """
        
    
    #TODO: OPTIONAL METHOD
    def describeRawData(self,rawData:Iterable[pd.DataFrame])->Dict[str,Union[Iterable,float]]:
        """Carries out some simple statistics on the new raw data such as the size of the dataframes, 
        percentage of certain basins, number of wells, etc. If not implemented ,the default behaviour in the base class is to return the shapes of 
        all data frames in raw data.
        
        Args:
            rawData (Iterable[pd.DataFrame]): Iterable of data frames that represents raw data.
        
        Returns:
            Dict[str,Union[Iterable,float]]: Dictionary containing pairs of ("Measure/Metric Name":Val)
        """

       

    def extractRawData(self)->Iterable[pd.DataFrame]:
        """Extracts the raw data from any data source such as a database, csv files, etc. 
        Returns:
            Iterable[pd.DataFrame]: Data frames representing the raw data.
        """
        


    
    def processData(self,rawData:Iterable[pd.DataFrame])->Iterable[pd.DataFrame]:
        """Carries out any necassary pre-processing on the raw data, 
        such as removing data errors, unit conversion, aliasing, arps fitting, peak shifting etc.
        
        Args:
            rawData (Iterable[pd.DataFrame]): Data frames representing the new raw data that were returned from the extractRawData method.
        
        Returns:
            Iterable[pd.DataFrame]: Processed data frames.
        """
        

