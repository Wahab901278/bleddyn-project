import pandas as pd
class DataIngestion:
    def __init__(self,file_path):
        self.file_path=file_path
    def read_data(self):
        df=pd.read_csv(self.file_path)

        return df

if __name__=='__main__':
    di=DataIngestion('data/_Amazon_Clothing_Sales_2025 DS12  - Amazon_Clothing_Sales_2025 (1).csv')
    print(di.read_data())