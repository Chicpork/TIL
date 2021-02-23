import matplotlib.pyplot as plt
import numpy as np

from dataset_generator import dataset_generator
import basic_nodes as nodes

# dataset preparation
feature_data = np.random.normal(size=(100, 1))
dataset_gen = dataset_generator(1, n_sample=100, noise=0.5)
dataset_gen.set_coefficient([0, 5])
dataset = dataset_gen.make_dataset()
x_data, y_data = dataset[:, 1], dataset[:, 2]
plt.scatter(x_data, y_data)
plt.show()

# model implementation
node1 = nodes.mul_node()

# squre error loss implementation
node2 = nodes.minus_node()
node3 = nodes.square_node()
node4 = nodes.mean_node()

# hyperparameter
lr = 0.01  # learning rate
th = -1    # arbitrary theta
loss_list = []
th_list = []

# Mini-batch size
batch_size = 16 # minibatch
n_batch = int(np.ceil(len(x_data)/batch_size))
total_iteration = 30
epochs = np.ceil(total_iteration/n_batch).astype(int)

for _ in range(epochs):
    idx_np = np.arange(len(x_data))
    np.random.shuffle(idx_np)
    x_data = x_data[idx_np]
    y_data = y_data[idx_np]
    
    for batch_idx in range(n_batch):
        if batch_idx is n_batch-1:
            X = x_data[batch_idx*batch_size :]
            Y = y_data[batch_idx*batch_size :]
        else:
            X = x_data[batch_idx*batch_size : (batch_idx+1)*batch_size]
            Y = y_data[batch_idx*batch_size : (batch_idx+1)*batch_size]

        Z1 = node1.forward(th, X)
        Z2 = node2.forward(Y, Z1)
        L = node3.forward(Z2)
        J = node4.forward(L)

        dL = node4.backward(1)
        dZ2 = node3.backward(dL)
        dY, dZ1 = node2.backward(dZ2)
        dTh, dX = node1.backward(dZ1)

        th = th - lr*np.sum(dTh)

        th_list.append(th)
        loss_list.append(J)

fig, ax = plt.subplots(2, 1, figsize = (15, 5))
ax[0].plot(th_list)
ax[1].plot(loss_list)
plt.style.use('seaborn')
plt.show()