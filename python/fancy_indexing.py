# ================================================================= #
#                        1.Fancy Indexing                           #
# ================================================================= #
# Fancy Indexing is an advanced indexing method in Numpy, which is still available in pytorch.
#%%
#Import needed library
import numpy as np
#%%
### Usage 1 : 1-D Arrays ###
#Create a 1-D array
a = np.arange(10)
#Using fancy indexing
chosen_a = a[[0, 3, 7]] #[0 3 7]
print(chosen_a)
# %%
### Usage 2 : 2-D Arrays ###
#Create a 2-D array
b = np.arange(24).reshape(4,6)
print(b)
#e.g.1 seperate the index using comma
chosen_b = b[0,0]
#e.g.2 Nesting using multiple index operators []
chosen_b = b[0][0]
#e.g.3 
chosen_b = b[[1,2],[3,4]] #[ 9 16] (1,3) & (2,4)
# %%
### Usage 3: Mixing fancy indexing and Slicing ###
#Using fancy indexing
chosen_b_mix = b[1:3,[3,4]] #[[9 10],[15 16]]
print(chosen_b_mix)
# %%
### Usage 4: Bool indexing ###
#Create a bool array
bool_index = a % 2 == 0 #[ True False  True False  True False  True False  True False]
#Using fancy indexing
chosen_a_bool = a[bool_index] #[0 2 4 6 8]

