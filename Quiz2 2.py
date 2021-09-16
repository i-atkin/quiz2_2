#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:44:50 2021

@author: i_atkin
"""

import numpy as np
import matplotlib.pyplot as plt

#user input and function to get Fibonacci sequence array to N
sequence = input("Fibonacci Sequence Number: ")

list = []
def fib(sequence):
    n1 = 0
    n2 = 1
    counter = 0

    while counter < int(sequence):
        list.append(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        counter += 1

fib = fib(sequence)

#turning the list into a numpy array 
seq = np.asarray(list)
print("Fibonacci Sequence to  " + str(sequence)+ " terms.")
print(seq)

#golden ratio and creating a plot 
gratio=[seq[i] / float(seq[i-1]) for i in range(2,len(seq))]
plot(gratio)
