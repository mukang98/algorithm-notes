import torch
#v2版本重点在于模块化与合理化部分代码，争取形成更有逻辑的个人代码风格。
# 设置随机种子，保证实验可复现
torch.manual_seed(42)
def generate_data(num_samples=100):
    X = torch.rand(2, num_samples) * 40 - 20
    true_params = torch.tensor([7.6, 8.457])
    Y = torch.matmul(true_params, X) + torch.randn(num_samples) * 1.5   
    return X, Y

# 前向传播
def forward(X, W, b):
    return torch.matmul(W, X) + b

# 均方误差损失
def mse_loss(y_pred, y_true):
    return torch.mean((y_true - y_pred) ** 2) # 真实值 - 预测值

def compute_gradients(X_batch, Y_batch, W, b):
    y_pred = forward(X_batch, W, b) 
    error = y_pred - Y_batch #求偏导
    W_grad = (2 / X_batch.size(1)) * torch.matmul(error, X_batch.T) 
    b_grad = (2 / X_batch.size(1)) * torch.sum(error)
    return W_grad, b_grad

def train_sgd(X, Y, W, b, num_epochs=5, batch_size=4, lr=0.001):
    for epoch in range(num_epochs):
        num_samples = X.size(1)
        indices = torch.randperm(num_samples)
        for i in range(0, num_samples, batch_size):
            batch_indices = indices[i:i+batch_size]
            X_batch = X[:,batch_indices]
            Y_batch = Y[batch_indices]
            W_grad, b_grad = compute_gradients(X_batch, Y_batch, W, b)

            W -= lr * W_grad
            b -= lr * b_grad

        loss_value = mse_loss(forward(X, W, b), Y)
        print(f'Epoch {epoch + 1}, Loss: {loss_value.item():.4f}')
    return W, b

def main():
    #生成数据
    X, Y = generate_data(200)
    #初始化模型参数、训练参数
    W = torch.rand(2)
    b = torch.zeros(1)
    batch_size = 5
    lr = 0.001
    num_epochs= 5

    W, b = train_sgd(X, Y, W, b, num_epochs, batch_size, lr)
    # 输出训练结果
    print("\n训练结束，最终参数：")
    print("W =", W)
    print("b =", b)

if __name__ == '__main__':
    main()




