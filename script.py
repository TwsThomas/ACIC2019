import numpy as np
import pandas as pd
import os

from joblib import Parallel, delayed

def try_process(data_id=1, folder='data/'):

    data_name = 'testdataset{}.csv'.format(data_id)
    out_name = 'testdataset{}_res.txt'.format(data_id)
    data_path = os.path.join(folder, data_name)
    output_path = os.path.join(folder, out_name)
    print('read data in', data_path)
    data = np.array(pd.read_csv(data_path, low_memory=False))
    res = np.array(data.shape)
    print('results is ', res)
    print('save it in', output_path)
    np.savetxt(output_path, res)
  


Parallel(n_jobs=2)(delayed(try_process)(i) 
                   for i in range(1,3))
