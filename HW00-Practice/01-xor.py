#!/usr/bin/env python
#-*- conding: utf-8-*-

import numpy as np
import matplotlib.pyplot as plt

class linear_perceptron:
    def __init__(self, train_data_f):
        self.train_data_f = train_data_f
        
    def train(self):
        # open train_data
        train_f = open("train_data.in", "r")
    
        train_data = []
        for line in train_f:
            data = []
            for x in line.split():
                data.append(int(x))
            train_data.append([np.matrix([data[0], data[1], 1]), data[2]])
        
        # boundary
        n_vec = np.matrix([0, 0, 0])
        learn_rate = 1
    
        # record last change
        data_len = len(train_data)
        ch = data_len - 1
        over = False
    
        while (over == False):
            for i in xrange(0, data_len):
                n_vec, changed = self.learn(n_vec, train_data[i], learn_rate)
                if changed:
                    ch = i
                elif ch == i:
                    over = True
                    break
            if over:
                break
        
        boundary = n_vec.tolist()
        self.plot(boundary, train_data)

    def learn(self, n_vec, train_data, learn_rate):
        d_of_p = (int)(np.inner(n_vec, train_data[0]))
        if train_data[1] == 0 and d_of_p <= 0:
            n_vec = n_vec + learn_rate*train_data[0]
            return n_vec, True
        elif train_data[1] == 1 and d_of_p >= 0:
            n_vec = n_vec - learn_rate*train_data[0]
            return n_vec, True
        else:
            return n_vec, False
    
    
    def getdata(self, train_data):
        data0_x = []
        data0_y = []
        data1_x = []
        data1_y = []
    
        for i in train_data:
            point = [(i[0].tolist())[0][0], (i[0].tolist())[0][1]]
            if i[1] == 0:
                data0_x.append(point[0])
                data0_y.append(point[1])
            else:
                data1_x.append(point[0])
                data1_y.append(point[1])
    
        return data0_x, data0_y, data1_x, data1_y
    
    def plot(self, boundary, train_data):
        a = (float)(boundary[0][0])/boundary[0][1] * (-1)
        b = (float)(boundary[0][2])/boundary[0][1] * (-1)
        
        x = np.linspace(-5, 15, 200)
        y = a*x + b
        
        c0_px, c0_py, c1_px, c1_py = self.getdata(train_data)
        plt.axis([-0.5, 1.5, -0.5, 1.5])
        plt.plot(x, y)
        plt.plot(c0_px, c0_py, 'ro')
        plt.plot(c1_px, c1_py, 'go')
        plt.show()
        
    

if __name__ == '__main__':
    x = linear_perceptron("asdf")
    x.train()
