import sys

import pandas as pd
import re

data = pd.read_csv(sys.argv[1],skiprows=1,encoding="gbk",engine='python',sep='\t',delimiter=None, index_col=False,header=None,skipinitialspace=True)

data = data[data[2] == 'mRNA']
data[0] = data[0].str.replace('chr?','',regex=True)
data[8] = data[8].str.split('[=;]',expand=True)[1]

data.sort_values(by=[0,3],inplace=True)
data = data.loc[:, [0, 8, 3, 4, 6]]

data.reset_index(drop=True, inplace=True)

data[9] = data.index+1 
data.to_csv(sys.argv[2], sep="\t", header=None,index=False)
