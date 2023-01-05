import pandas as pd
import sys
gff = pd.read_csv(sys.argv[1],sep='\t',header=None)
print(gff.head())
n=1
for i in range(467,507):
    s = 'NC_054'+str(i)+'.1'
    gff[0] = gff[0].replace(s,str(n),)
    n+=1
    print(s)
gff.to_csv(sys.argv[2],sep='\t',header=None,index=None)
print(gff)
    # exit(0)
