import pandas as pd
import numpy as np

#df = pd.read_csv('seoul_cctv.csv',encoding='cp949')
'''
#clustering group num
for z in range(100729):
    globals()['g'+str(z+1)] = [] #g1=[], g2=[], ... , g100729=[]

#clustering by scope
row_num = np.arange(0,0.2641,0.001)
col_num = np.arange(0,0.3841,0.001)

for x in range(263):
    for y in df['위도']:
        if 37.430 < y < 37.430 + x:
            globals()['g'+str(x+1)].append(y)
'''

#row_num = np.arange(37.430, 37.6941, 0.001)
'''
g=dict()
for z in range(300):
    g[z] = []
    
'''


#algorithm to get mean of each coordinate value
def mean(lst):
    result = 0
    for val in lst:
        result += val
    return result/len(lst)

a=[1,2]
b=[3,4]
c=[5,6]

x=[a,b,c] #[[1,2],[3,4],[5,6]]

p1=[] #[1,3,5]
p2=[] #[2,4,6]

for i in range(len(x)):
    print(x[i][0])
    p1.append(x[i][0])
    #p2.append(x[i][1])
    #print(x[i][1])
    print('------')

print(mean(p1)) # 3.0
#print(mean(p2)) # 4.0
