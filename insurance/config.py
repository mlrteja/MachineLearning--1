import pymongo
import pandas as pd
import numpy as np
import json
import os,sys
from dataclasses import dataclass

@dataclass
class environmentvariable:
      mongo_db_url:str=os.getenv("mongo_db_url")


env_var=environmentvariable()
mongo_client=pymongo.MongoClient(env_var.mongo_db_url)
target_column="expenses"
print(env_var.mongo_db_url)

