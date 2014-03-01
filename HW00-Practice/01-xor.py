#!/usr/bin/env python
#-*- conding: utf-8-*-

import numpy as np
import matplotlib.pyplot as plt

def learn(n_vec_0, n_vec_1, train_data, learn_rate):
    d_of_p0 = (int)(np.inner(n_vec_0, train_data[0]))
    d_of_p1 = (int)(np.inner(n_vec_1, train_data[0]))
    if train_data[1] == 0 and d_of_p0 <= d_of_p1:
        n_vec_0 = n_vec_0 + learn_rate*train_data[0]
        n_vec_1 = n_vec_1 - learn_rate*train_data[0]
        return n_vec_0, n_vec_1, True
    elif train_data[1] == 1 and d_of_p0 >= d_of_p1:
        n_vec_0 = n_vec_0 - learn_rate*train_data[0]
        n_vec_1 = n_vec_1 + learn_rate*train_data[0]
        return n_vec_0, n_vec_1, True
    else:
        return n_vec_0, n_vec_1, False


def getdata(train_data):
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


if __name__ == '__main__':
    #train_data = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [1, 1, 0]]
    train_data = [[np.matrix([0, 1, 1]), 1], 
                  [np.matrix([1, 1, 1]), 0]]

    # two classes, two variable, learing rate
    n_vec_0 = np.matrix([0, 0, 0])
    n_vec_1 = np.matrix([0, 0, 0])
    learn_rate = 1

    # record last change
    data_len = len(train_data)
    ch = data_len - 1
    over = False

    while (over == False):
        for i in xrange(0, data_len):
            n_vec_0, n_vec_1, changed = learn(n_vec_0, n_vec_1, train_data[i], learn_rate)
            if changed:
                ch = i
            elif ch == i:
                over = True
                break
        if over:
            break
    
    boundary = (n_vec_0 - n_vec_1).tolist()
    a = (float)(boundary[0][0])/boundary[0][1] * (-1)
    b = (float)(boundary[0][2])/boundary[0][1] * (-1)
    
    x_data = [x/10.0 for x in xrange(-5 , 15)]
    y_data = [a*x + b for x in x_data]
    
    c0_px, c0_py, c1_px, c1_py = getdata(train_data)
    plt.axis([-0.5, 1.5, -0.5, 1.5])
    plt.plot(x_data, y_data)
    plt.plot(c0_px, c0_py, 'ro')
    plt.plot(c1_px, c1_py, 'go')
    plt.show()
