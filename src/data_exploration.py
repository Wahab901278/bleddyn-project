import missingno as msno
import numpy as np
import matplotlib.pyplot as plt
import os
class DataExploration:
    def __init__(self,df):
        self.df=df
        self.shape=df.shape
        self.dtypes=df.dtypes
    
    def null_check(self):
        return self.df.isnull().sum()

    def null_visualization(self):
        fig=msno.matrix(self.df)
        os.makedirs('/Users/fireflylaptops/Desktop/bledyyn-project/visualizations',exist_ok=True)
        plt.savefig('visualizations/null_values_visualization.png')
        return fig
    def types_of_columns(self):
        numerical_columns=self.df.select_dtypes(include=np.number).columns.tolist()
        categorical_columns=self.df.select_dtypes(include='object').columns.tolist()

        return numerical_columns,categorical_columns
    
    def info_of_data(self):
        return self.df.info()