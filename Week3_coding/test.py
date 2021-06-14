#Import Library 
from csp import * 
from random import shuffle
import random 
random.seed(123)
#Import sys 
import sys 
# sys.path.insert(0, '/Users/chenyan/.local/lib/python3.8/site-packages')
# sys.path.insert(0, '/Users/chenyan/opt/anaconda3/lib/python3.8/site-packages')
# sys.path.insert(0, '/usr/local/Cellar/protobuf/3.15.8/libexec/lib/python3.9/site-packages')
import numpy as np
import pandas as pd
# Reference : http://aima.cs.berkeley.edu/python/csp.html

def solve_semi_magic(algorithm = backtracking_search,**args):
    """ From CSP class in csp.py
        vars        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
                    """
    csp_vars = [f'V{d}' for d in range(1,10)]
    #print("csp_vars: ", csp_vars)
    csp_domains = { v:list(range(1,4)) for i,v in enumerate(csp_vars) }
    #print('csp_domains0: ' , csp_domains)
    csp_neighbors = {
        'V1': ['V2', 'V3', 'V4', 'V7', 'V5', 'V9'],
        'V2': ['V1', 'V3', 'V5', 'V8'],
        'V3': ['V1', 'V2', 'V5', 'V7', 'V6', 'V9'],
        'V4': ['V1', 'V7', 'V5', 'V6'],
        'V5': ['V1', 'V2', 'V3', 'V4', 'V6', 'V7', 'V8', 'V9'],
        'V6': ['V3', 'V4', 'V5', 'V9'],
        'V7': ['V1', 'V4', 'V5', 'V3', 'V8', 'V9'],
        'V8': ['V7', 'V2', 'V5', 'V9'],
        'V9': ['V1', 'V5', 'V3', 'V6', 'V7', 'V8'],
    }

    random.shuffle(csp_vars)
    csp_domains = list(csp_domains.items())
    #print('csp_domains1: ' , csp_domains)
    random.shuffle(csp_domains)
    csp_domains = dict(csp_domains)
    #print('csp_domains2: ' , csp_domains)
    for o in csp_domains.values(): random.shuffle(o)
    csp_neighbors = list(csp_neighbors.items())
    #print('csp_neighbors0: ' , csp_neighbors)
    random.shuffle(csp_neighbors)
    csp_neighbors = dict(csp_neighbors)
    #print('csp_neighbors1: ' , csp_neighbors)
    for o in csp_neighbors.values(): random.shuffle(o)
        
    def csp_constraints(A, a, B, b):
        return a != b

    #########################################
    # define the CSP instance
    csp = CSP(csp_vars, csp_domains, csp_neighbors,
              csp_constraints)

    # run the specified algorithm to get an answer (or None)
    ans = algorithm(csp, **args)
#     print('number of assignments', csp.nassigns)
    assign = csp.infer_assignment()
#     if assign: for x in sorted(assign.items()): print(x)
    return csp




"""
1. The parameter of backtracking_search methods : from csp.py 
def backtracking_search(csp,
                        select_unassigned_variable = first_unassigned_variable,
                        order_domain_values = unordered_domain_values,
                        inference = no_inference):

2. mcv - If true, use Most Constrained Variable Heuristic
   lcv - If true, use Least Constraining Value Heuristic
   fc  - If true, use Forward Checking
   mac - If true, use Maintaining Arc Consistency. 

"""


"""
 2. Experiment solving this problem with the various solution methods, 
 rang-ing from pure backtracking and its various enhancements/heuristics 
 such as variable and value orderings, forward checking, etc
"""
n = 100
print("----------------------------------------------------------------")

#Method1 unssigned variable,unordered, no inference
ns1 = []
method1 = solve_semi_magic(backtracking_search, select_unassigned_variable = first_unassigned_variable, 
                       order_domain_values = unordered_domain_values, inference = no_inference)
for _ in range(n): ns1.append(method1.nassigns)
print("----------------Method1 unssigned variable,unordered, no inference-------------")
print(f"\t\t Method1 : average assignments \t\t  {np.mean(ns1)}")

#Method2 mrv,unordered, no inference
ns2 = []
method2 = solve_semi_magic(backtracking_search, select_unassigned_variable = mrv, 
                 order_domain_values = unordered_domain_values, inference = no_inference)
for _ in range(n): ns2.append(method2.nassigns)
print("----------------Method2 mrv, unordered , no inference-------------")
print(f"\t\t Method2 : average assignments \t\t  {np.mean(ns2)}")

#Method3 unssigned variable,lcv, no inference
ns3 = []
method3 = solve_semi_magic(backtracking_search, select_unassigned_variable = first_unassigned_variable, 
                 order_domain_values = lcv, inference = no_inference)
for _ in range(n): ns3.append(method3.nassigns)
print("----------------Method3 first assigned, lcv, no inference-------------")
print(f"\t\t Method1 : average assignments \t\t  {np.mean(ns3)}")

ns4 = []
method4 = solve_semi_magic(backtracking_search, select_unassigned_variable = first_unassigned_variable, 
                 order_domain_values = unordered_domain_values, inference = forward_checking)
for _ in range(n): ns4.append(method4.nassigns)
print("----------------Method4 first unssigned variable, unordered, forward_checking-------------")
print(f"\t\t Method1 : average assignments \t\t  {np.mean(ns4)}")


ns5 = []
method5 = solve_semi_magic(backtracking_search, select_unassigned_variable = first_unassigned_variable, 
                 order_domain_values = unordered_domain_values, inference = mac)
for _ in range(n): ns5.append(method5.nassigns)
print("----------------Method5 first unassigned,unordered, mac, AC-3-------------")
print(f"\t\t Method1 : average assignments \t\t  {np.mean(ns5)}")

ns6 = []
method6 = solve_semi_magic(backtracking_search, select_unassigned_variable = mrv, 
                 order_domain_values = lcv, inference = mac)
for _ in range(n): ns6.append(method6.nassigns)
print("----------------Method6 mrv,lcv, mac, AC-3-------------")
print(f"\t\t Method1 : average assignments \t\t  {np.mean(ns6)}")

"""
3. Look  at  the  number  of  assignments  attempted  by  each  algorithm,  
thatshould  give  you  some  idea  of  the  effectiveness  of  the  methods  
on  thisproblem.   Elaborate  on  your  findings  from  these  results,  
i.e.,  what  you understand

ANS : 
In my experiment, I set n = 100 , that means the problem will be iterated 100 times.
Based on the average of 100 iterations performance, I will evaluate the effectiveness of 
each methods. 

Finding :
1. Method1 is pure backtracking algorithm , the average number of assignments is 177, 

Understanding : 

"""