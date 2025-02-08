#%%
import torch
torch.manual_seed(42)
# 模拟数据
X = torch.rand(2,100, dtype=torch.float32)*40 - 20
src_params = torch.tensor([7.6, 8.457], dtype=torch.float32)
Y = torch.matmul(src_params,X)
Y += torch.randn(Y.shape) * 1.5
# %%
W = torch.rand(2, dtype=torch.float32)
b = torch.zeros(1)
def function(X):
    return torch.matmul(W, X) + b