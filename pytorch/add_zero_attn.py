#%%
# ================================================================= #
#                        1.add_zero_attn                            #
# ================================================================= #

# This design aims to prevent the undesirable uniform distribution of attention weights that can occur when there's no valid attention target. 
# By introducing a dummy token, the model avoids distributing attention uniformly across irrelevant positions, 
# which could lead to meaningless outputs. Instead, the dummy token ensures that attention is directed towards a specific target, 
# even if that target's value contribution is zero, 
# thereby maintaining the integrity of the model's output and preventing it from generating nonsensical results in situations where valid attention targets are lacking.

import torch
import numpy as np

embedding_dim = 8
batch_size = 1
num_heads = 2
seq_len = 4 #N_target
net = torch.nn.MultiheadAttention(embedding_dim, num_heads, add_zero_attn=True)

mask_dummpy = torch.from_numpy(np.array([[True, True, True, True],
                                  [False, True, True, True],
                                  [False, False, True, True],
                                  [False, False, False, True]])).float() * -10000.0 #attn_mask (N_target, N_source)
# print(mask)
mask_normal = torch.from_numpy(np.array([[False, True, True, True],
                                      [False, False, True, True],
                                      [False, False, False, True],
                                      [False, False, False, False]])).float() * -10000.0 
for i in range(seq_len):
    x = torch.ones(seq_len, batch_size, embedding_dim, requires_grad=True) # (4, 1, 8)
    o, w = net(x, x, x, attn_mask=mask_dummpy)   
    print(w)
    break
# tensor([[[0.0000, 0.0000, 0.0000, 0.0000, 1.0000],
#          [0.4454, 0.0000, 0.0000, 0.0000, 0.5546],
#          [0.3080, 0.3080, 0.0000, 0.0000, 0.3839],
#          [0.2355, 0.2355, 0.2355, 0.0000, 0.2936]]], grad_fn=<MeanBackward1>)
# if add_zero_attn = False, then the attention weights will be like this:
# tensor([[[0.2500, 0.2500, 0.2500, 0.2500],
#          [1.0000, 0.0000, 0.0000, 0.0000],
#          [0.5000, 0.5000, 0.0000, 0.0000],
#          [0.3333, 0.3333, 0.3333, 0.0000]]], grad_fn=<MeanBackward1>)

# The first row of the tensor, [0.2500, 0.2500, 0.2500, 0.2500], indicates that the attention weights are evenly distributed across all four positions.

# %%
