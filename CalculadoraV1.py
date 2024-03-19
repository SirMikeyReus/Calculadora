def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def calcular():
    operacion = input("Ingrese la operación (+, -, *, /): ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == '+':
        print("Resultado:", suma(num1, num2))
    elif operacion == '-':
        print("Resultado:", resta(num1, num2))
    elif operacion == '*':
        print("Resultado:", multiplicacion(num1, num2))
    elif operacion == '/':
        print("Resultado:", division(num1, num2))
    else:
        print("Operación no válida.")

calcular()
