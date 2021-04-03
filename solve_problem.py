#!/usr/bin/env python3

import openjij as oj

    
def solve_problem(model, feed_dict):
    # convert to qubo
    qubo, offset = model.to_qubo(feed_dict=feed_dict)
    # solve with OpenJij (SA)
    sampler = oj.SASampler(num_reads=10)
    response = sampler.sample_qubo(Q=qubo)
    # take mininum state
    dict_solution = response.first.sample
    solution = model.decode_sample(dict_solution, vartype='BINARY', feed_dict=feed_dict)    
    broken = solution.constraints(only_broken=True)
    return solution, broken