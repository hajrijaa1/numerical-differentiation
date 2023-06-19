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
file = 'grupaB.dat'
df = pd.read_csv(file, sep=" ", header=None)
for index, row in df.iterrows():
    f[row[0]] = row[1]
h = list(f.keys())[1] - list(f.keys())[0]
num_diferenciranje(f, h)

