"""
Realizar una calculadora en donde se le pida al usuario una operación
Validar (“+” , “-” , “/”, “*”) en caso de no ser ninguno de esos especificar error

(+) -> Suma
(-) -> Resta
(/) -> Dividir
(*) -> Multiplicar

Luego de tener el operador, pedir dos números y hacer la operación correspondiente.

"""
operacion = input("Ingrese que tipo de operación quiere hacer: + para suma, - para resta, / para division, * para multiplicación")
while operacion not in "+-/*":
    operacion = input("Ingrese que tipo de operación quiere hacer: + para suma, - para resta, / para division, * para multiplicación")

primer_numero = int(input("Ingrese un número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

match operacion:
    case "+":
        resultado = primer_numero + segundo_numero
    case "-":
        resultado = primer_numero - segundo_numero
    case "/":
        while segundo_numero == "0":
            segundo_numero = int(input("No se puede dividir por cero, ingrese otro número: "))
        resultado = primer_numero / segundo_numero 
    case "*":
        resultado = primer_numero * segundo_numero

print(f"{primer_numero} {operacion} {segundo_numero} = {resultado}")