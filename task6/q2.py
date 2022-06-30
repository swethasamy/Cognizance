import pandas as pd
import numpy as np
   

data = pd.read_csv("Q2-Dataset.csv")
   

data.replace(to_replace = 'NaN' , value = 55)