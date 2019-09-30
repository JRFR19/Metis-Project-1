import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
import pickle
import seaborn as sns



def get_data(week_nums):
    url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_{}.txt"
    dfs = []
    col_names= ['CA','UNIT','SCP','STATION','LINENAME','DIVISION','DATE','TIME','DESC','ENTRIES','EXITS']
    for week_num in week_nums:
        file_url = url.format(week_num)
        dfs.append(pd.read_csv(file_url, sep=",", header=0, names = col_names, parse_dates=[['DATE', 'TIME']]))
    return pd.concat(dfs)
        
week_nums = [190504, 190511, 190518, 190525]

df = get_data(week_nums)