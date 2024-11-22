#%%
#动态传参
class ModelTrain:
    def __init__(self, lr, epoch_num, step_num) -> None:
        self.lr = lr
        self.epoch_num = epoch_num
        self.step_num = step_num
    def train(self, data):
        for _ in range(len(data)):
            print(f"epoch_nums为{self.epoch_num}")
            print(f"step_num为{self.step_num}")
data_test = [1,2,3,4]
details = {"lr":1e-7, "epoch_num":5 , "step_num": 500}
model = ModelTrain(**details)
#**details 是 Python 的解包语法，表示将字典 details 中的键值对解包成关键字参数，传递给一个函数或类。
result = model.train(data_test)
print(result) 
# %%
