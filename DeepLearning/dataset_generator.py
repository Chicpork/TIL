import numpy as np

class dataset_generator:

    # feature_dim : n 차원
    def __init__(self, feature_dim, n_sample = 100, noise = 0):
        if feature_dim == None:
            raise ValueError
        
        self._feature_dim = feature_dim
        self._n_sample = n_sample
        self._noise = noise
        self._coefficient_list = None

        self._init_coefficient()

    def _init_coefficient(self):
        self._coefficient_list = [0] + [1 for _ in range(self._feature_dim)]

    def set_coefficient(self, coefficient_list):
        if len(coefficient_list) != self._feature_dim+1:
            raise ValueError

        self._coefficient_list = coefficient_list

    def make_dataset(self):
        x_data = np.zeros(shape = (self._n_sample, 1))
        y_data = np.zeros(shape = (self._n_sample, 1))

        for coeffi_idx in range(1, self._feature_dim + 1):
            feature_data = self._coefficient_list[coeffi_idx]*np.random.normal(size=(self._n_sample, 1))
            x_data = np.hstack((x_data, feature_data))
            y_data += self._coefficient_list[coeffi_idx]*feature_data
        
        y_data += self._coefficient_list[0] + np.random.normal(loc = 0,
                                                               scale = self._noise,
                                                               size=(self._n_sample, 1))

        self._dataset = np.hstack((x_data, y_data))
        return self._dataset