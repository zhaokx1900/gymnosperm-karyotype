
import sys

import pandas as pd
import re

data = pd.read_csv(sys.argv[1],skiprows=1,encoding="gbk",engine='python',sep='\t',delimiter=None, index_col=False,header=None,skipinitialspace=True)

data[0] = data[0].astype(str)
data[0] = '6cpa_' + data[0]
#sgi01_ pta02_ wmi03_ gmo04_ twa05_ cpa06_ gbi07_ tch08_ cgi09_ tgr10_ mgl11_ lka12_

data.to_csv(sys.argv[2], sep="\t", header=None,index=False)

