import matplotlib.pyplot as plt
import os
import seaborn as sns



class DataVisualization:
    def __init__(self,df):
        self.df=df

    def visualize_distributions_of_numerical_columns(self,numerical_columns):
        fig1,axes=plt.subplots(2,4,figsize=(16,6))
        axes = axes.flatten() 
        for i,col in enumerate(numerical_columns):
            axes[i].hist(self.df[col])
            axes[i].set_title(col)
        os.makedirs('/Users/fireflylaptops/Desktop/bledyyn-project/visualizations',exist_ok=True)
        plt.savefig('visualizations/distribution_of_numeric_columns_visualization.png')
        
        fig2,axes=plt.subplots(2,4,figsize=(16,6))
        axes = axes.flatten() 
        for i,col in enumerate(numerical_columns):
            sns.boxplot(self.df[col],ax=axes[i])
        os.makedirs('/Users/fireflylaptops/Desktop/bledyyn-project/visualizations',exist_ok=True)
        plt.savefig('visualizations/distribution_of_numeric_columns_visualization(boxplot).png')
        return fig1,fig2
    

    def visualize_distributions_of_categorical_columns(self,categorical_columns):
        fig1,axes=plt.subplots(2,4,figsize=(16,6))
        axes = axes.flatten() 
    
        for i,col in enumerate(categorical_columns):
            print(self.df[col].value_counts())
            axes[i].bar(self.df[col])
            axes[i].set_title(col)
        os.makedirs('/Users/fireflylaptops/Desktop/bledyyn-project/visualizations',exist_ok=True)
        plt.savefig('visualizations/distribution_of_categorical_columns_visualization.png')
    
    def heatmap(self,numerical_columns):
        numerical_columns=self.df[numerical_columns]
        correlation_matrix=numerical_columns.corr()
        plt.figure(figsize=(16,6))
        fig1=sns.heatmap(correlation_matrix,annot=True)
        fig = fig1.get_figure()
        fig.savefig('visualizations/correlation_heatmap1.png')
        return fig