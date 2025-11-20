class DataCleaning:
    def __init__(self,df):
        self.df=df
    
    def fix_missing_values(self,method_to_fix):
        columns_with_missing=[]
        for name,value in self.df.isnull().sum().items():
            if value>0:
                columns_with_missing.append(name)
        print(columns_with_missing)
        for column in columns_with_missing:
            self.df[column]=self.df[column].fillna(method=method_to_fix)
        
        return self.df
    
    def fix_duplicates(self):
        no_of_duplicates=self.df.duplicated().sum()
        print(f"The number of duplicates are:{no_of_duplicates}")
        if no_of_duplicates>0:
            print("Dropping these duplicates from data...")
            self.df=self.df.drop_duplicates()
        return self.df
        

