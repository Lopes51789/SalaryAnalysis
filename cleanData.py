import pandas as  pd
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


class DataFrame():
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def getStats(self):
        print("Stats from the dataset")
        return self.df.describe()
    
    def getNullSum(self):
        print("Null Values in the dataset")
        return self.df.isnull().sum()
    
    def getDescription(self):
        print("Dataset description")
        return self.df.info()
    
    def getCorrelation(self):
        print("Correlation of the dataset")
        return self.df.corr()
    
    def toCsv(self):
        return self.df.to_csv("cleaned_data.csv")

    def toJson(self):
        filename = "cleaned_data.json"
        self.df.to_json(filename, orient='records')
        return filename

    def getColumnNames(self):
        print("Column names")
        return self.df.columns
    
    def convertCategoricalToNumeric(self):
        categorical_cols = self.df.select_dtypes(include=['category', 'object']).columns
        label_encoder = LabelEncoder()
        for row in categorical_cols:
            if type(row) == str:
                self.df[row] = label_encoder.fit_transform(self.df[row])

        return label_encoder
    def removeNullValues(self):
        self.df.dropna(inplace=True)

    def removeDuplicateCategories(self):
        for index, row in self.df.iterrows():
            # do something with the row
            if row["Education Level"] == "Bachelor's" or row["Education Level"] == "Master's":
                self.df.at[index, "Education Level"] += " Degree"

        



def test():
    salary_data = DataFrame("Salary_Data.csv")
    
    #salary_data.toJson()

    #print(salary_data.getCorrelation())
    #print(salary_data.getStats())
    #print(salary_data.getNullSum())
    #salary_data.getDescription()
    salary_data.removeNullValues()
    salary_data.removeDuplicateCategories()
    salary_data.convertCategoricalToNumeric()

    #print(salary_data.df[salary_data.df.isnull().any(axis=1)])

if __name__ == "__main__":
    test()
    pass