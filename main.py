#!/usr/bin/env python3

import matplotlib.pyplot as plt

import make_energy as me
import make_instance as mi
import solve_problem as sop
import visualize_solution as vs


if __name__ == '__main__':
    # set problem
    num_city, distance = mi.make_instance()
    # set costs & constraints
    model = me.make_energy(num_city=num_city, distance=distance)
    # set hyperparameters
    parameters = {}
    for i in range(num_city):
        parameters['h_a_{}'.format(i)] = 0.0001
        parameters['h_b_{}'.format(i)] = 0.0001
    parameters['h_c'] = 0.0001
    # set empty list for plot in parameter space
    x = [parameters['h_a_1']]
    y = [parameters['h_b_1']]
    for _ in range(10):
        # solve with OpenJij
        solution, broken = sop.solve_problem(model=model, feed_dict=parameters)
        # check broken 
        print(broken)
        if len(broken) == 0:
            break
        for key in broken.keys():
            parameters[key] += parameters['h_c'] * broken[key][1] 
        parameters['h_c'] *= 2
        x.append(parameters['h_a_1'])
        y.append(parameters['h_b_1'])
    print(x)
    print(y)
    plt.plot(x, y, color='black')
    plt.plot(x[0], y[0], marker='.', color='blue', markersize=20)
    plt.plot(x[-1], y[-1], marker='.', color='red', markersize=20)
    plt.show()
    # visualize result
    vs.visualize_solution(solution, num_city)
