# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

for i in range(3):

    x = np.linspace(start=i, stop=i+1, num=100)
    y = np.random.randint(0, 100, 100)
    z = np.random.normal(0, 1, 100)

    df = pd.DataFrame({'x': x, 'y': y, 'z': z})

    if i == 1:
        sep = ';'
    else:
        sep = ','

    df.to_csv(f'df{i}.csv', sep=sep, index=False)
