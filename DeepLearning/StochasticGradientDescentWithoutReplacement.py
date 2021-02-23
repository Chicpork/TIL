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

# hyperparameter
epochs = 5 # total epoch
lr = 0.01  # learning rate
th = -1    # arbitrary theta
loss_list = []
th_list = []

for _ in range(epochs):
    random_idx = np.arange(len(x_data))
    np.random.shuffle(random_idx)
    x_data = x_data[random_idx]
    y_data = y_data[random_idx]

    for data_idx in range(len(x_data)):
        x, y = x_data[data_idx], y_data[data_idx]

        z1 = node1.forward(th, x)
        z2 = node2.forward(y, z1)
        l = node3.forward(z2)

        dz2 = node3.backward(1)
        dy, dz1 = node2.backward(dz2)
        dth, dx = node1.backward(dz1)

        th = th - lr*dth

        th_list.append(th)
        loss_list.append(l)

fig, ax = plt.subplots(2, 1, figsize = (15, 5))
ax[0].plot(th_list)
ax[1].plot(loss_list)
plt.style.use('seaborn')
plt.show()