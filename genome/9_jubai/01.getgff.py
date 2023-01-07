import sys

import pandas as pd
import re

data = pd.read_csv(sys.argv[1],skiprows=0,encoding="gbk",engine='python',sep='\t',delimiter=None, index_col=False,header=None,skipinitialspace=True)

data = data[data[2] == 'mRNA']
data[0] = data[0].str.replace('Chr?','',regex=True)
data[8] = data[8].str.split('[=;]',expand=True)[1]
data[10] = data[8].str.split('.',expand=True)[0]

data[3] = data[3].astype(int)
data[4] = data[4].astype(int)
data[9] = data[4]-data[3]
data.loc[data.groupby(10)[9].idxmax()]
data.drop_duplicates(subset=[10], keep='first', inplace=True)

data.sort_values(by=[0,3],inplace=True)
data = data.loc[:, [0, 8, 3, 4, 6]]


data.reset_index(drop=True, inplace=True)
data[9] = data.index+1 
data.to_csv(sys.argv[2], sep="\t", header=None,index=False)
