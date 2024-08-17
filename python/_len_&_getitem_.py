#%%
# ================================================================= #
#                       1. __len__ & __getitem__                    #
# ================================================================= #
# By implementing the __len__ and __getitem__ magic methods, the class instances can 
# be indexed and have their length calculated, similar to how sequences work.
import pandas as pd
df = pd.DataFrame(
    {"name":["Mary","John","Friede"],
     "Math":[88,99,65],
     "English":[89,75,95]}
)
class DataSet:
    def __init__(self, df):
        self.data = df
    def __len__(self):
        return len(self.data["name"])
    def __getitem__(self, index):
        item_math = self.data["Math"].iloc[index]
        item_en = self.data["English"].iloc[index]
        return item_math, item_en
test = DataSet(df)
print(len(test))
print(test[2])
    

# %%
