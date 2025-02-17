#该版本为PyTorch 内置的优化器（Momentum、RMSProp、Adam）并且采用 mini-batch 训练方式实现
#除了优化器的使用方式以外，也要关注mini-batch训练 使用到的dataloader
#%%
#1.1导入依赖
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

import numpy as np
import matplotlib.pyplot as plt

torch.manual_seed(42)  # 固定随机种子
#%%
# 1.2 模拟数据集
# 生成 100 个数据点
N = 100
X = torch.linspace(0, 9, N).unsqueeze(-1)     # shape [100,1]
y = 3 * X + 2 + torch.randn_like(X) * 2.0     # 加点噪声, shape [100,1]
# %%
# 1.3 创建 Dataset & DataLoader
class SimpleDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y
    def __len__(self):
        return len(self.X)
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 构建 Dataset
dataset = SimpleDataset(X, y)

# 构建 DataLoader
# 这里我们设定 batch_size=10, shuffle=True 实现随机小批量迭代
batch_size = 10
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# %%
# 2. 定义模型（线性回归）
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        # 这里假设输入1维，输出1维
        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        # 前向传播
        return self.linear(x)
#%%
#3. 训练函数 (mini-batch)
# 每个 epoch 遍历所有 mini-batch：
# 前向：y_pred = model(x_batch)
# 计算损失：loss = MSE(y_pred, y_batch)
# 反向传播：loss.backward()
# 更新：optimizer.step()
# 清空梯度：optimizer.zero_grad()
def train_model(optimizer_type="sgd_momentum", lr=0.01, epochs=50):
    # 1) 实例化模型
    model = LinearModel()
    
    # 2) 定义损失函数
    criterion = nn.MSELoss()
    
    # 3) 根据不同的 optimizer_type，创建对应的优化器
    if optimizer_type == "sgd_momentum":
        optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9)
    elif optimizer_type == "rmsprop":
        optimizer = optim.RMSprop(model.parameters(), lr=lr, alpha=0.9) 
        # 注意: PyTorch里 RMSProp 的衰减系数对应参数名是 alpha, 默认0.99
    elif optimizer_type == "adam":
        optimizer = optim.Adam(model.parameters(), lr=lr, betas=(0.9, 0.999))
    else:
        raise ValueError("Unknown optimizer_type")
    
    # 4) 训练循环
    loss_history = []
    for epoch in range(epochs):
        epoch_loss = 0.0
        for (x_batch, y_batch) in dataloader:
            # 清空梯度
            optimizer.zero_grad()

            # 前向
            y_pred = model(x_batch)
            # 计算损失
            loss = criterion(y_pred, y_batch)
            
            # 反向传播
            loss.backward()
            # 更新
            optimizer.step()

            epoch_loss += loss.item()
        
        # 记录一个 epoch 的平均损失
        avg_loss = epoch_loss / len(dataloader)
        loss_history.append(avg_loss)
        
        # 这里简单打印一下
        # print(f"Epoch {epoch+1}/{epochs}, Loss={avg_loss:.4f}")
    
    return model, loss_history
#%%
# 4. 运行对比
# 不同优化器设置
optimizers = ["sgd_momentum", "rmsprop", "adam"]
lr = 0.01
epochs = 50

results = {}
for opt_name in optimizers:
    model_trained, loss_hist = train_model(
        optimizer_type=opt_name, lr=lr, epochs=epochs
    )
    # 取出最终的 w, b
    # 因为我们 linear 是 nn.Linear(1, 1)，要拿它的权重、偏置
    w = model_trained.linear.weight.item()
    b = model_trained.linear.bias.item()
    final_loss = loss_hist[-1]
    results[opt_name] = (model_trained, w, b, loss_hist, final_loss)

# 打印结果
for opt_name, (model_trained, w, b, _, final_loss) in results.items():
    print(f"{opt_name:>12s} => w={w:.4f}, b={b:.4f}, final_loss={final_loss:.4f}")

# %%
#5. 可视化损失曲线
plt.figure(figsize=(8, 5))
for opt_name, (_, _, _, loss_hist, _) in results.items():
    plt.plot(loss_hist, label=opt_name)
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Loss Curves for Different Optimizers (Mini-Batch)")
plt.legend()
plt.show()

# %%
#6. 预测效果检查
# 假设我们看 Adam 训练的结果
model_adam = results["adam"][0]  # 直接拿 Adam 训练好的模型
print(model_adam)
x_line = torch.linspace(0, 9, 100).unsqueeze(-1)
with torch.no_grad():  # 不需要计算梯度
    y_pred_line = model_adam(x_line)

# 绘制数据与预测曲线
plt.scatter(X.numpy(), y.numpy(), label="Data")
plt.plot(x_line.numpy(), y_pred_line.numpy(), 'r-', label="Model Prediction (Adam)")
plt.legend()
plt.show()
# %%
