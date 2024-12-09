#!/usr/bin/env python3

import math

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if(b==0):
        raise ValueError("No se puede dividir entre 0")
    else:
        return a/b

def potencia(a,b):
    return a**b

def logaritmo(a,base):
    try:
        logar = math.log(a,base)
    except:
        print("No hay solución al problema")
    if logar==None:
        raise ValueError("No hay solución al problema")
    else:
        return logar


operaciones = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division,
    '**':potencia,
    'log':logaritmo}

def calculadora():
    print("Calculadora básica en Python")
    print("Operaciones disponibles: +, -, *, /, **, log")

    # 
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Pedir el operador
    operador = input("Introduce el operador (+, -, *, /, **, log): ")

    # Usar el diccionario para realizar la operación
    operacion = operaciones.get(operador)

    if operacion:  # Verifica si el operador es válido
        resultado = operacion(num1, num2)
        print(f"El resultado de {num1} {operador} {num2} es {resultado}")
    else:
        print("Operador no válido. Usa +, -, *, /, **, log.")

# Llamar a la calculadora
calculadora()