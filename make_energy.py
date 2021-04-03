#!/usr/bin/env python3

import numpy as np
from pyqubo import Array, Constraint, Placeholder

def make_energy(num_city, distance):
    # set binary variables
    x = Array.create('x', shape=(num_city, num_city), vartype='BINARY')
    # # fix variables for preprocess
    # x = np.array(x)
    # x[0][0] = 1
    # for i in range(1, num_city):
    #     x[0][i] = 0
    # for t in range(1, num_city):
    #     x[t][0] = 0
    # set hyperparameters
    lambda_a = []
    lambda_b = []
    for i in range(num_city):
        lambda_a.append(Placeholder('h_a_{}'.format(i)))
        lambda_b.append(Placeholder('h_b_{}'.format(i)))
    lambda_c = Placeholder('h_c')
    # set one-hot encoding for time
    h_a = []
    for t in range(num_city):
        tmp = sum([x[t][i] for i in range(num_city)]) - 1
        h_a.append(tmp)
    # set one-hot encoding for city
    h_b = []
    for i in range(num_city):
        tmp = sum([x[t][i] for t in range(num_city)]) - 1
        h_b.append(tmp)
    # set function for augmented lagrangian function
    h_c = sum([h_a[i] ** 2 for i in range(num_city)])
    h_c += sum([h_b[i] ** 2 for i in range(num_city)])
    # convert to constraint
    for i in range(num_city):
        h_a[i] = Constraint(h_a[i], label='h_a_{}'.format(i))
        h_b[i] = Constraint(h_b[i], label='h_b_{}'.format(i))
    h_c = Constraint(h_c, label='h_c')
    # set objective function
    obj = 0
    for t in range(num_city):
        for i in range(num_city):
            for j in range(num_city):
                obj += distance[i][j] * x[t][i] * x[(t+1)%num_city][j]
    # compute total energy
    hamiltonian = obj + lambda_c / 2 * h_c
    hamiltonian += sum([lambda_a[i]*h_a[i] for i in range(num_city)])
    hamiltonian += sum([lambda_b[i]*h_b[i] for i in range(num_city)])
    # compile
    model = hamiltonian.compile()
    return model
