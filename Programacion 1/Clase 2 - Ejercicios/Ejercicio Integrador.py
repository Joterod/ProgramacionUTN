"""
La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener 
los siguientes datos: 
1. El tipo (validar "barbijo", "jabón" o "alcohol") 
2. El precio: (validar entre 100 y 300) 
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades) 
4. La marca y el Fabricante. 

Se debe informar lo siguiente: 
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. 
B. Del ítem con más unidades, el fabricante. 
C. Cuántas unidades de jabones hay en total.
"""
precio_mayor = None
cantidad_barbijos = None
fabricante_barbijos = None
mas_unidades = None
mas_unidades_fabricante = None
unidades_jabon_total = 0

for i in range(5):
    tipo = input("Ingrese el tipo de producto: barbijo/jabón/alcohol ")
    while tipo != "barbijo" and tipo != "jabón" and tipo != "alcohol":
        tipo = input("Error, ingrese el tipo de producto: barbijo/jabón/alcohol ")
    precio = int(input("Ingrese el precio del producto: entre 100 y 300"))
    while not 100 <= precio <= 300:
        precio = int(input("Error, ingrese el precio del producto: entre 100 y 300"))
    cantidad = int(input("Ingrese la cantidad de unidades (Entre 1 y 1000)"))
    while not 1 <= cantidad <= 1000:
        cantidad = int(input("Error, ingrese la cantidad de unidades (Entre 1 y 1000)"))
    marca = input("Ingrese el nombre de la marca: ")
    fabricante = input("Ingrese el nombre del fabricante: ")

    if tipo == "barbijo":
        if precio_mayor is None or precio_mayor < precio:
            precio_mayor = precio
            cantidad_barbijos = cantidad
            fabricante_barbijos = fabricante

    if mas_unidades is None or mas_unidades < cantidad:
        mas_unidades = cantidad
        mas_unidades_fabricante = fabricante

    if tipo == "jabón":
        unidades_jabon_total += cantidad

# A
print(f"El barbijo mas caro es fabricado por {fabricante_barbijos}, con {cantidad_barbijos} unidades en stock")

# B
print(f"El producto con mas stock es fabricado por {mas_unidades_fabricante}")

# C
print(f"La cantidad total de jabones es de {unidades_jabon_total} unidades")