# -*- coding = uft-8 -*-
# @File     : 00_2_1_try_auto_differenciate.py
# @Time     : 2022/5/7 10:06  
# @Author   : Samuel HONG
# @Description : 尝试自动微分
# @Version  :

import torch

x = torch.ones(2, 2, requires_grad=True)
# print(x)
y = x + 2
print(y)
print(y.grad_fn)

z = y * y * 3
out = z.mean()
print(z)
print(out)
