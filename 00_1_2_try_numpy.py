# -*- coding = uft-8 -*-
# @File     : 00_1_2_try_numpy.py
# @Time     : 2022/5/6 21:29  
# @Author   : Samuel HONG
# @Description : try_numpy_with_torch
# @Version  :

import numpy as np
import torch

a = np.ones(5)

# torch是可以限定数据精度的，不知道np可不可以
# dtype=torch.double
b1 = torch.Tensor(a)
b2 = torch.from_numpy(a)
print('size b1:', b1.size())
print('size a:', np.array(a).size)

a1 = np.ones((5, 3))
print(np.array(a1).size)

# 可以这样写：
a0 = torch.empty(size=torch.Tensor(a).size())
print(a0.size())
# 如何去识别size，配上呢
c = torch.empty(5)
torch.add(b1, b2, out=c)
print(a, b1, b2, c, sep='\n', end='\n\n')

np.add(a, 1, out=a)
print('add_tensor:', a, b1, sep='\n')
