import numpy as np

class ValueSet():
    def __init__(self):
        data = np.load("dataset//trainedData.npz")
        self.X_train = data['arr_0']
        self.y_train = data['arr_1']
        print("loaded X", self.X_train.shape)
        print("loaded Y", self.y_train.shape)

    def __len__(self):
        return len(self.y_train)

    def __getitem__(self, index):
        return (self.X_train[index], self.y_train[index])

dat = ValueSet()