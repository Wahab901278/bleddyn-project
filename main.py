import pandas as pd
from src.data_ingestion import DataIngestion
from src.data_exploration import DataExploration
from src.data_cleaning import DataCleaning
from src.data_visualization import DataVisualization



di=DataIngestion('data/_Amazon_Clothing_Sales_2025 DS12  - Amazon_Clothing_Sales_2025 (1).csv')
df=di.read_data()
print("="*50)
print("Data Exploration")
print("="*50)
de=DataExploration(df)
print('-'*50)
print("The shape of data is:",de.shape)
print('-'*50)
print('-'*50)
print("The data types of columns are:\n",de.dtypes)
print('-'*50)
print('-'*50)
print("The information of data:\n",de.info_of_data())
print('-'*50)
print('-'*50)
print("The missing values in data:\n",de.null_check())
print('-'*50)
print('-'*50)
print("The visulaization of missing values:\n",de.null_visualization())
print('-'*50)
print('-'*50)
print("The numerical and categorical columns in the data are:")
numerical_columns,categorical_columns=de.types_of_columns()
print("Numerical columns:\n",numerical_columns)
print("Categorical columns:\n",categorical_columns)
print('-'*50)

print("Data Cleaning Started...")
dc=DataCleaning(df)
df=dc.fix_missing_values('ffill')
df=dc.fix_duplicates()

print("Data Cleaning Done!")

print("Number of numerical columns",len(numerical_columns))


dv=DataVisualization(df)
figure1,figure2=dv.visualize_distributions_of_numerical_columns(numerical_columns)
