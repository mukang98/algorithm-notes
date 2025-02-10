#[几种常用torch随机初始化]
import torch
a = torch.rand(2,3) #1 - 范围为 [0, 1), 矩阵size为([2,3])
b = torch.randn(2,3) #2 - X∼N(0,1)，矩阵size为([2,3])
c = torch.randint(0, 10, (2,3) ) #3 - 整数，范围为 [0, 10), 矩阵size为([2,3])
d = torch.randperm(10)#4 - 整数[0, 10)上随机数列, tensor size为([10])
e = torch.normal(0, 1, (2,3))#5 -  X∼N(0,1)，矩阵size为([2,3])
