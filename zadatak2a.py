import pandas as pd
import numpy as np
import math

def num_diferenciranje(f, h):
    print("Diferenciranje unaprijed")
    for i in f.keys():
        if (i+h) in f.keys():
            f_xi = (f[i+h] - f[i])/h
            print("f'(" + str(i) + ") = " + str(f_xi))

    print("Diferenciranje unazad")
    for i in f.keys():
        if (i - h) in f.keys():
            f_xi = (f[i] - f[i-h])/h
            print("f'(" + str(i) + ") = " + str(f_xi))

    print("Centralno diferenciranje")
    for i in f.keys():
        if (i - h) in f.keys() and (i+h) in f.keys():
            f_xi = (f[i+h] - f[i-h])/(h * 2)
            print("f'(" + str(i) + ") = " + str(f_xi))

f = dict()
f[3.4] = 0.294118
f[3.5] = 0.285714
f[3.6] = 0.277778
h = list(f.keys())[1] - list(f.keys())[0]
num_diferenciranje(f, h)

