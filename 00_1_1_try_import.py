# -*- coding = uft-8 -*-
# @File     : 00_1_1_try_import.py
# @Time     : 2022/5/6 16:11  
# @Author   : Samuel HONG
# @Description : 
# @Version  :

import torch

x1 = torch.rand(5, 3)
x2 = torch.empty(5, 3)
x3 = torch.zeros(5, 3, dtype=torch.long)
x4 = torch.tensor([5.5, 3])
x5 = torch.ones(5, 3, dtype=torch.double)

x6 = torch.randn_like(x5, dtype=torch.float)
print('x6', x6.size(), end='\n')

# 张量的加法？
x7 = torch.rand(5, 3)
print('x6,x7 add result way1: \n', x6 + x7, end='\n')
print('x6,x7 add result way2: \n', torch.add(x6, x7), end='\n')
result = torch.empty(5, 3)
torch.add(x6, x7, out=result)
print('x6,x7 add result way3: \n', result, end='\n')
x7.add_(x6)
print('x6,x7 add result way4: \n', x7, end='\n')
