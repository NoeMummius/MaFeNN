# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 08:04:21 2020

@author: Noé Muñoz Pérez
"""

# We need this to initialize python packages
import random

class Perceptron:
    def __init__(self,input_number,step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size

    def predict(self,inputs):
        weighted_average = sum(w*elm for w,elm in zip(self._w,inputs))
        if weighted_average > 0:
            return 1
        return 0

    def train(self,inputs,ex_output):
        output = self.predict(inputs)
        error = ex_output - output
        if error != 0:
            self._w = [w+self._eta*error*x for w,x in zip(self._w,inputs)]
        return error

#!/usr/bin/env python
#from perceptron import Perceptron

## Datos de hombres y mujeres
## Estatura, peso, hombros, cadera, longitud de los brazos y longitud de las piernas
input_data = [[170,56,1],
              [172,63,0],
              [160,50,1],
              [170,63,0],
              [174,66,0],
              [158,55,1],
              [183,80,0],
              [182,70,0],
              [165,54,1],
              [160,55,48,92,52,88,1],
              [160,55,88,92,52,85,1],
              [167,59,39,88,53,85,1]]

## Creamos el perceptron
pr = Perceptron(7,0.1) # Perceptron con 3 entradas
weights = [] # Lista con los pesos
errors = []  # Lista con los errores

## Fase de entrenamiento
for _ in range(100):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1] # Agregamos un uno por default
        weights.append(pr._w)
        err = pr.train(inp,output)
        errors.append(err)

h = float(input("Introduce tu estatura en centimetros.- "))
w = float(input("Introduce tu peso en kilogramos.- "))
s = float(input("Introduce la anchura de tus hombros en centímetros")) 
h = float(input("Introduce la medida de tu cadera en centímetros"))
a = float(input("Introduce la longitud de tus brazos en centímetros"))
l = float(input("Introduce la longitud de tus piernas en centímetros"))

if pr.predict([1,h,2]) == 1: print ("Mujer")
else: print ("Hombre")

#print """
#Nota: El resultado puede estar incorrecto.
#Esto puede ser debido a sesgo en la muestra, o porque es imposible separar
#a hombres y mujeres perfectamente basados unicamente en talla y peso."""

## Fase de graficacion
import imp

can_plot = True
try:
    imp.find_module('matplotlib')
except:
    can_plot = False

if not can_plot:
    print ("No es posible graficar los resultados porque no tienes matplotlib")
    sys.exit(0)
    pass

import matplotlib.pyplot as plt

plt.plot(errors)
plt.show()
