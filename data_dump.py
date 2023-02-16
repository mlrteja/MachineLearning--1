import pymongo # pip install pymongo
import pandas as pd
import json


import urllib
client = pymongo.MongoClient("mongodb+srv://lakshmiraviteja:"+urllib.parse.quote("Memsphd99@") +"@cluster0.tcc0blz.mongodb.net/?retryWrites=true&w=majority")


DATA_FILE_PATH = (r"D:\insurance project\MachineLearning--1\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")
    print(df.head())
    print(type(df))
    #df=df.reset_index(drop = True, inplace = True)
    

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    
   
    



   