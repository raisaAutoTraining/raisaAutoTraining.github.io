




class MyModel(AutoTrainingModel):
    """A class that represents a ML model.
    """

    
    def constructModelSets(self,processedData:Iterable[pd.DataFrame])->ModelDataSetsHolder:
        """Builds the model's training and test sets.
        
        Args:
            processedData (Iterable[pd.DataFrame]): Processed data frames returned from DataManager.processData        
        Returns:
            ModelDataSetsHolder: The model's training and test sets wrapped in a ModelSetHolder object. 
            You can refer to the "ModelSetsHolder" class in the "model.py" module for more details.
        """
        
    
    def trainAndEvalModel(self,modelSets:ModelDataSetsHolder,firstModel:object,latestModel:object)->ModelEvalOutput:
        """Trains the model and compares its accuracy to the both the first model and the latest models, 
        to detect any abnormal drop in accuracy that may be caused by some bug or data error.
        
        Args:
            modelSets (ModelDataSetsHolder): Training and test sets.
            firstModel (object): The initial model at the time of registering the package.
            latestModel (object): The last model pushed to production.
        Returns:
            ModelEvalOutput: Object representing the model evaluation result.
        """
        
        


    def getInitialModelRelativePath(self): #relative path from the code file implementing this method.
        """ 
        Returns:
        str: the relative path of the initial model that was built and trained during the prototyping phase.
        The path should be relative to the the directory containing this file. 
        """
        


    def loadModelFromPath(self,path:str):
        """ Returns the model object representing the model file in the path provided.
        Args:
            path (str): full path to the model file (pkl,h5,etc.).
        Returns:
        Object: model object (keras model object, sklearn, pytorch, etc.) 
        """
        
    

    
    def saveModelToPath(self,modelObj:object,path:str):
        """ Saves the passed model object to a model file (h5,pkl,etc.) in the path provided.
        Args:
            modelObj (object): model object (keras model object, sklearn, pytorch, etc.)
            path (str): full path to the model file.
        """
        pass  