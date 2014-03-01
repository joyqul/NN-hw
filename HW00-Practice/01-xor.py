#!/usr/bin/env python
#-*- conding: utf-8-*-

import numpy as np

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
    
    print n_vec_0, n_vec_1
