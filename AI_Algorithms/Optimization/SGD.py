#%%
#v1版本为对sgd理解的mini-batch版本。存在自己写代码的3个严重问题。
#1.全局变量作为定义函数的输入。
#2.更新参数和计算梯度的逻辑耦合，且实现方式较差。
#3.loss的入参
#4.缺少打乱数据步骤
import torch
torch.manual_seed(42)
# 模拟数据
X = torch.rand(2,100)*40 - 20
src_params = torch.tensor([7.6, 8.457])
Y = torch.matmul(src_params,X)
Y += torch.randn(Y.shape) * 1.5
print(Y.shape)
# %%    
#初始化待训练参数
W = torch.rand(2)
b = torch.zeros(1)
#定义前向传播
def function(X):
    return torch.matmul(W, X) + b
#%%
def loss(X, Y):
    return sum((Y - function(X))**2)/X.size(1)
#%%
batch_size = 1
lr = 0.001
#%%
start = 0
for _ in range(int(X.size(1)/batch_size)):
    W -= lr * torch.sum(2* (function(X[:,start:start+batch_size]) - Y[start:start+batch_size])*X[:,start:start+batch_size]/batch_size, dim = 1) / batch_size
    b -=lr * torch.sum(2* (function(X[:,start:start+batch_size]) - Y[start:start+batch_size])/batch_size, dim = 0) / batch_size
    start += batch_size
print(W,b)

#%%
