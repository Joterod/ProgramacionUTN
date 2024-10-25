"""
Realizar una calculadora en donde se le pida al usuario una operación
Validar (“+” , “-” , “/”, “*”) en caso de no ser ninguno de esos especificar error

(+) -> Suma
(-) -> Resta
(/) -> Dividir
(*) -> Multiplicar

Luego de tener el operador, pedir dos números y hacer la operación correspondiente.

"""
def sumar(a, b):
    return a+b
def restar(a, b):
    return a-b
def dividir(a, b):
    if b != 0:
        return a/b
    else:
        return print("No se puede dividir por cero")
def multiplicar(a, b):
    return a*b


operacion = input("Ingrese que tipo de operación quiere hacer: + para suma, - para resta, / para division, * para multiplicación")
while operacion not in "+-/*":
    operacion = input("Ingrese que tipo de operación quiere hacer: + para suma, - para resta, / para division, * para multiplicación")

primer_numero = int(input("Ingrese un número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

match operacion:
    case "+":
        resultado = sumar(primer_numero, segundo_numero)
    case "-":
        resultado = restar(primer_numero, segundo_numero)
    case "/":
        resultado = dividir(primer_numero, segundo_numero)
    case "*":
        resultado = multiplicar(primer_numero, segundo_numero)

print(f"{primer_numero} {operacion} {segundo_numero} = {resultado}")

