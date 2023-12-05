def calcular_salario (horas, tarifa):
    if horas <= 40:
        salario = horas * tarifa
    else :  
        salario = (horas-40)*tarifa*1.5 + tarifa *40
    return salario

while True:
    try:
        horas = float (input ("introduzaca las horas: "))
        tarifa = float (input ("introduzca la tarifa por hora: "))
        break
    except: 
        print("error, debe ingresar un numero")

salario = calcular_salario(horas,tarifa)
print (salario)

