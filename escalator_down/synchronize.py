import pandas as pd
import numpy as np
import os

acc_list = os.listdir("acc")
p_list = os.listdir("baro")
print (acc_list)
for i in range(len(acc_list)):
    acc = pd.read_csv("acc/" + acc_list[i])['acc'].values
    pre = pd.read_csv("baro/" + p_list[i])

    store = [0]

    for j in range(len(acc)-11):
        if((np.std(acc[j:j+10],ddof=1)<0.5) and (np.std(acc[j+1:j+11],ddof=1)>0.5)):
            store.append(j)
        if((np.std(acc[j:j+10],ddof=1)>0.5) and (np.std(acc[j+1:j+11],ddof=1)<0.5)):
            store.append(j)
    store.append(len(pre))
    print (store)
    for k in range(len(store)-1):
        if(k%2 == 0):
            pre[store[k]:store[k+1]].to_csv(str(i) + str(k) + '.csv', index= False)

