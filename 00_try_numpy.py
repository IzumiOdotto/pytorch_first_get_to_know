# -*- coding = uft-8 -*-
# @File     : 00_try_numpy.py
# @Time     : 2022/5/6 21:29  
# @Author   : Samuel HONG
# @Description : try_numpy_with_torch
# @Version  :

import numpy as np
import torch

a = np.ones(5)
b = torch.from_numpy(a)
print(a, b)

np.add(a, 1, out=a)
print(a, b)
