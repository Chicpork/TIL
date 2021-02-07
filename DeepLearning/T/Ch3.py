#%%
from . import basic_nodes

#%%
test_x = [1, 2, 3, 4, 5]
node = basic_nodes.mean_node()
z = node.forward(test_x)
dx = node.backward(2)
print(dx)
