#%%
# ================================================================= #
#                       1. apply                                    #
# ================================================================= #
# The apply function in pandas allows you to apply a function along either axis (rows or columns) of a DataFrame or Series. 
# It’s particularly useful when you want to perform operations on the data that aren’t natively supported by pandas methods.
import pandas as pd
df = pd.DataFrame(
    {"name":["Mary","John","Friede"],
     "Math":[88,99,65],
     "English":[89,75,95]}
)
# Usage-1:
#Apply a custom function and pass additional arguments using the args parameter.
def scoring(row, factor):
    return factor*row["Math"] + row["English"]
df["Total score math"] = df.apply(scoring, axis = 1, args = (1.2,))
print(df)
#%%
# Usage-2:
#Use a lambda expression to define the function logic directly.
df["Total score en"] = df.apply(lambda row : row["Math"]+ 1.2*row["English"], axis=1)
print(df)
# %%
