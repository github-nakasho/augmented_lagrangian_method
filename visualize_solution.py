#!/usr/bin/env python3

import pprint as pp

def visualize_solution(solution, num_city):
    # visualize = []
    # fixed = [0] * num_city
    # fixed[0] = 1
    # visualize.append(fixed)
    # for t in range(1, num_city):
    #     tmp = [0]
    #     for i in range(1, num_city):
    #         tmp.append(solution.array('x', (t, i)))
    #     visualize.append(tmp)
    # pp.pprint(visualize)
    
    for t in range(num_city):
        tmp = []
        for i in range(num_city):
            tmp.append(solution.array('x', (t, i)))
        print(tmp)