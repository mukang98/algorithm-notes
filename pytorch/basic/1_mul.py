# %%
# ================================================================= #
#                        1.乘法                                     #
# ================================================================= #
import torch
#%%
#1.矩阵乘法
#1.1 torch.mm()适用于 2D 张量（即矩阵）之间的乘法。
a = torch.randn(3, 5)
b = torch.randn(5, 6)
ans = torch.mm(a,b)
#1.2 torch.bmm()适用于 3D 张量（即批量矩阵）之间的乘法
c = torch.randn(10, 3, 4)  # 形状为 (10, 3, 4)
d = torch.randn(10, 4, 5)  # 形状为 (10, 4, 5)
result = torch.bmm(c, d)   # 输出形状为 (10, 3, 5)
#1.3 torch.matmul() & '@'适用于 不同维度的张量乘法
e = torch.randn(10, 3, 4)  # 形状 (10, 3, 4)
f = torch.randn(10, 4, 5)  # 形状 (10, 4, 5)
result = torch.matmul(e, f)  # 输出形状 (10, 3, 5)
result = e @ f
print(result)
#%%
#2.点积
#2.1 torch.dot()只适用于 1D 向量（一维张量）
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
result = torch.dot(x, y)
#2.2 torch.inner() 适用于 任意维度的张量
a = torch.tensor([[1, 2, 3], [4, 5, 6]])
b = torch.tensor([[7, 8, 9], [10, 11, 12]])
result = torch.inner(a, b)
# 结果为 tensor([[ 50,  68],
#                [122, 167]])
#%%
#3.对应元素相乘
#torch.mul() & torch.multiply() & '*'
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
result = torch.multiply(x, y)
result = torch.mul(x, y)
result = x * y
# %%
#4.矩阵-向量乘法
#4.1 torch.mv()专门处理 矩阵-向量 乘法。输入必须是二维张量和一维向量，乘法结果是一个新的向量。
matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])
vector = torch.tensor([7, 8, 9])
result = torch.mv(matrix, vector)
#4.2 torch.matmul & '@'也可以
result = torch.matmul(matrix, vector)
result = matrix @ vector