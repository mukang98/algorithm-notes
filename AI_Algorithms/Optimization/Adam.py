#该版本为手动实现momentum, RMSprop, Adam，用于理解与学习
#%%
import torch
import torch.nn.functional as F
#%%
#1.准备数据
# 固定随机种子，保证每次运行结果一致
torch.manual_seed(42)

#生成 10 个点，x 从 0 到 9
X = torch.arange(10, dtype=torch.float32)
# 模拟真实 y=3x+2 加一点噪声
y = 3 * X + 2 + torch.randn_like(X) * 1.0  # 噪声幅度可自行调节
N = len(X)
#%%
#2.定义通用的前向与损失
def forward(x, w, b):
    """ 线性模型 y_pred = w*x + b """
    return w * x + b

def mse_loss(y_pred, y_true):
    """ MSE 损失 """
    return F.mse_loss(y_pred, y_true)  # 等价于 (y_pred - y_true).pow(2).mean()
#%%
#3. Momentum 手动实现下面的函数 train_momentum 将会手动执行训练循环。每个 epoch 中：
# 前向：y_pred = forward(X, w, b)
# 计算 loss = mse_loss(y_pred, y)
# loss.backward() 得到 w.grad、b.grad
# 依据 Momentum 更新公式，用 v_w、v_b 追踪动量
# w.data、b.data 做更新
# w.grad.zero_()、b.grad.zero_() 清空梯度，准备下一次迭代
def train_momentum(X, y, lr=0.01, beta=0.9, epochs=100):
    # 可训练参数 w, b，初始化
    w = torch.randn(1, requires_grad=True)  # 标量
    b = torch.zeros(1, requires_grad=True)
    
    # 动量变量，与 (w, b) 形状一致
    v_w = torch.zeros_like(w)
    v_b = torch.zeros_like(b)

    loss_history = []

    for epoch in range(epochs):
        # 1. 前向计算
        y_pred = forward(X, w, b)
        # 2. MSE损失
        loss = mse_loss(y_pred, y)
        
        # 3. 反向传播: 计算 dw, db
        loss.backward()

        # 获取梯度 (PyTorch 会把梯度存在 w.grad, b.grad 中)
        dw = w.grad
        db = b.grad

        # 4. Momentum 更新
        # v = beta*v + (1-beta)*grad
        v_w = beta*v_w + (1 - beta)*dw
        v_b = beta*v_b + (1 - beta)*db
        # 参数更新: theta = theta - lr * v
        w.data -= lr * v_w
        b.data -= lr * v_b

        # 5. 清空梯度
        w.grad.zero_()
        b.grad.zero_()

        loss_history.append(loss.item())

    return w.item(), b.item(), loss_history

# 测试 Momentum
w_m, b_m, loss_m = train_momentum(X, y, lr=0.01, beta=0.9, epochs=100)
print(f"Momentum 训练结束: w={w_m:.4f}, b={b_m:.4f}, 最终损失={loss_m[-1]:.4f}")
print(loss_m)

# %%
#4. RMSProp 手动实现
def train_rmsprop(X, y, lr=0.01, beta=0.999, epsilon=1e-8, epochs=100):
    w = torch.randn(1, requires_grad=True)
    b = torch.zeros(1, requires_grad=True)

    # r_w, r_b 用于存梯度平方的滑动平均
    r_w = torch.zeros_like(w)
    r_b = torch.zeros_like(b)

    loss_history = []

    for epoch in range(epochs):
        # 前向与损失
        y_pred = forward(X, w, b)
        loss = mse_loss(y_pred, y)
        # 反向
        loss.backward()

        dw = w.grad
        db = b.grad

        # 更新 r
        r_w = beta * r_w + (1 - beta) * (dw ** 2)
        r_b = beta * r_b + (1 - beta) * (db ** 2)

        # 参数更新
        w.data -= lr * dw / torch.sqrt(r_w + epsilon)
        b.data -= lr * db / torch.sqrt(r_b + epsilon)

        # 清空梯度
        w.grad.zero_()
        b.grad.zero_()

        loss_history.append(loss.item())

    return w.item(), b.item(), loss_history

# 测试 RMSProp
w_r, b_r, loss_r = train_rmsprop(X, y, lr=0.01, beta=0.999, epsilon=1e-8, epochs=100)
print(f"RMSProp 训练结束: w={w_r:.4f}, b={b_r:.4f}, 最终损失={loss_r[-1]:.4f}")
# %%
def train_adam(X, y, lr=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8, epochs=100):
    w = torch.randn(1, requires_grad=True)
    b = torch.zeros(1, requires_grad=True)

    m_w = torch.zeros_like(w)  # 一阶矩
    v_w = torch.zeros_like(w)  # 二阶矩
    m_b = torch.zeros_like(b)
    v_b = torch.zeros_like(b)

    t = 0
    loss_history = []

    for epoch in range(epochs):
        t += 1
        y_pred = forward(X, w, b)
        loss = mse_loss(y_pred, y)
        loss.backward()

        dw = w.grad
        db = b.grad

        # 1) 一阶矩
        m_w = beta1*m_w + (1 - beta1)*dw
        m_b = beta1*m_b + (1 - beta1)*db
        # 2) 二阶矩
        v_w = beta2*v_w + (1 - beta2)*(dw ** 2)
        v_b = beta2*v_b + (1 - beta2)*(db ** 2)

        # 3) 偏差修正
        m_w_hat = m_w / (1 - beta1**t)
        m_b_hat = m_b / (1 - beta1**t)
        v_w_hat = v_w / (1 - beta2**t)
        v_b_hat = v_b / (1 - beta2**t)

        # 4) 更新参数
        w.data -= lr * m_w_hat / (torch.sqrt(v_w_hat) + epsilon)
        b.data -= lr * m_b_hat / (torch.sqrt(v_b_hat) + epsilon)

        w.grad.zero_()
        b.grad.zero_()

        loss_history.append(loss.item())

    return w.item(), b.item(), loss_history

# 测试 Adam
w_a, b_a, loss_a = train_adam(X, y, lr=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8, epochs=100)
print(f"Adam 训练结束: w={w_a:.4f}, b={b_a:.4f}, 最终损失={loss_a[-1]:.4f}")

# %%
