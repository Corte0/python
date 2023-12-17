#!/usr/bin/python3

import pyautogui as pyag
import time
import csv

archivo="15-16.csv"

datos=[]

with open(archivo, newline='') as csvfile:
    lector_csv = csv.DictReader(csvfile)
    for fila in lector_csv:
        datos.append(fila)

print ("datos por ser cargados")
for fila in datos: 
    #pyag.typewrite()
    print (f"pe:{fila['Periodo']}\tap:{fila['aporte']}\tCon:{fila['Contrib ']}\t")

input("Presiona Enter para continuar...")
print("tienes 5 segundos para seleccionar donde seran pegados los datos")
time.sleep(5)

for fila in datos: 
    pyag.typewrite(f"{fila['aporte']}\t{fila['Contrib ']}\tsuteryh\t")
  


