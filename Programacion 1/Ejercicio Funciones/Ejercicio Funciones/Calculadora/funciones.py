def suma(primer_numero,segundo_numero):
    resultado = f"El resultado de {primer_numero} + {segundo_numero} es:{primer_numero + segundo_numero}"
    return resultado
def resta(primer_numero,segundo_numero):
    resultado = f"El resultado de {primer_numero} - {segundo_numero} es: {primer_numero - segundo_numero}"
    return resultado
def division(primer_numero,segundo_numero):
    if segundo_numero != 0:
        resultado = f"El resultado de {primer_numero} / {segundo_numero} es: {primer_numero / segundo_numero}"
    else:
        resultado = "No es posible dividir por cero"
    return resultado
def multiplicacion(primer_numero,segundo_numero):
    resultado = f"El resultado de {primer_numero} * {segundo_numero} es: {primer_numero * segundo_numero}"
    return resultado
def potencia(primer_numero,segundo_numero):
    resultado = f"El resultado de {primer_numero} elevado a {segundo_numero} es: {primer_numero ** segundo_numero}"
    return resultado
def resto(primer_numero,segundo_numero):
    if segundo_numero != 0:
        resultado = f"El resultado de {primer_numero} % {segundo_numero} es: {primer_numero % segundo_numero}"
    else:
        resultado = "No es posible dividir por cero"
    return resultado

def factorial(operando):
    resultado = operando
    for numero in range (operando - 1, 1,-1):
        resultado = resultado * numero
    informe = f"El factorial de {operando} es: {resultado}"
    return informe

def factorial_recursivo(operando):
    if operando > 1:
        retorno = factorial_recursivo(operando - 1)
        resultado = operando * retorno
    else:
        resultado = 1
    return resultado

a = factorial_recursivo(8)
b = factorial(8)

print(a)
print(b)