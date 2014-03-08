#!/usr/bin/env python
#-*- conding: utf-8-*-

import numpy as np
import matplotlib.pyplot as plt

class linear_perceptron:
    def __init__(self, train_data_f, learn_rate = 1):
        self.train_data_f = train_data_f
        self.learn_rate = learn_rate
        self.train_data = []
        # boundary
        self.n_vec = np.matrix([0, 0, 0])
        
    def train(self):
        # open train_data
        train_f = open(self.train_data_f, "r")
    
        for line in train_f:
            data = []
            for x in line.split():
                data.append(int(x))
            self.train_data.append([np.matrix([data[0], data[1], 1]), data[2]])
        
        # record last change
        data_len = len(self.train_data)
        ch = data_len - 1
        over = False
    
        while (over == False):
            for i in xrange(0, data_len):
                if (self.learn(self.train_data[i])):
                    ch = i
                elif ch == i:
                    over = True
                    break
            if over:
                break
        
        self.boundary = self.n_vec.tolist()

    def learn(self, train_data):
        d_of_p = (int)(np.inner(self.n_vec, train_data[0][0]))

        if train_data[1] == 0 and d_of_p <= 0:
            self.n_vec = self.n_vec + self.learn_rate*train_data[0]
            return True
        elif train_data[1] == 1 and d_of_p >= 0:
            self.n_vec = self.n_vec - self.learn_rate*train_data[0]
            return True
        else:
            return False
    
    
    def getdata(self):
        self.data0_x = []
        self.data0_y = []
        self.data1_x = []
        self.data1_y = []
    
        for i in self.train_data:
            point = [(i[0].tolist())[0][0], (i[0].tolist())[0][1]]
            if i[1] == 0:
                self.data0_x.append(point[0])
                self.data0_y.append(point[1])
            else:
                self.data1_x.append(point[0])
                self.data1_y.append(point[1])
    
    def plot(self):
        a = (float)(self.boundary[0][0])/self.boundary[0][1] * (-1)
        b = (float)(self.boundary[0][2])/self.boundary[0][1] * (-1)
        
        x = np.linspace(-5, 15, 200)
        y = a*x + b
        
        self.getdata()

        plt.axis([-0.5, 1.5, -0.5, 1.5])
        plt.plot(x, y)
        plt.plot(self.data0_x, self.data0_y, 'ro')
        plt.plot(self.data1_x, self.data1_y, 'go')
        plt.show()
        
    

if __name__ == '__main__':
    x = linear_perceptron("train_data.in")
    x.train()
    x.plot()
