import pandas as pd
import numpy as np
import math
# Formule za diferenciranje unaprijed, unazad i centralno diferenciranje
def num_diferenciranje(f, h):
    formula_za_diferenciranje = int(input("Unesite formulu za numeričko diferenciranje: "))
    if formula_za_diferenciranje == 1:
        for i in f.keys():
            if (i+h) in f.keys():
                f_xi = (f[i+h] - f[i])/h
                print("f'(" + str(i) + ") = " + str(f_xi))
        
    elif formula_za_diferenciranje == 2:
        for i in f.keys():
            if (i - h) in f.keys():
                f_xi = (f[i] - f[i-h])/h
                print("f'(" + str(i) + ") = " + str(f_xi))
        
    elif formula_za_diferenciranje == 3:
        for i in f.keys():
            if (i - h) in f.keys() and (i+h) in f.keys():
                f_xi = (f[i+h] - f[i-h])/(h * 2)
                print("f'(" + str(i) + ") = " + str(f_xi))


print("Unesite 1 za unos tastaturom")
print("Unesite 2 za citanje fajla")
unos = int(input("Unos: "))
f = dict()
# Unos podataka s tastature
if unos == 1:
    unos_podataka = int(input("Unesite broj podataka za diferenciranje: "))
    for i in range(unos_podataka):
        X = float(input("Unesite " + str(i+1) + ". vrijednost x: "))
        F_x = float(input("Unesite " + str(i+1) + ". vrijednost f(x): "))
        f[X] = F_x
    h = list(f.keys())[1] - list(f.keys())[0]   
    num_diferenciranje(f, h)
# Učitavanje podataka s fajla
elif unos == 2:
    file = input("Fajl: ")
    df = pd.read_csv(file, sep=" ", header=None)
    for index, row in df.iterrows():
        f[row[0]] = row[1]
    h = list(f.keys())[1] - list(f.keys())[0]
    num_diferenciranje(f, h)

