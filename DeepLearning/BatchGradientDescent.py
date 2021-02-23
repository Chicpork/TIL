import matplotlib.pyplot as plt
import numpy as np

from dataset_generator import dataset_generator
import basic_nodes as nodes

# dataset preparation
feature_data = np.random.normal(size=(100, 1))
dataset_gen = dataset_generator(1, n_sample=100, noise=1)
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
epochs = 30 # total epoch
lr = 0.01  # learning rate
th = -1    # arbitrary theta
loss_list = []
th_list = []

for _ in range(epochs):
    X, Y = x_data, y_data

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