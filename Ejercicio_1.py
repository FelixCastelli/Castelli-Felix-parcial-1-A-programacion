def aplicarAumento(precio: float): # Funcion que recibe por parametro el precio
    aumento = precio * 0.05 # El calculo del aumento del 5%

    precio_con_aumento = precio + aumento # Le suma el aumento del 5% al precio ingresado
    return precio_con_aumento # Devuelve el precio con aumento

try:
    precio_ingresado = int(input("Ingrese el precio del cual desea calcular el (5%) de aumento: ")) # Le pido al usuario que ingrese el precio que quiera
except ValueError:
    precio_ingresado = int(input("ERROR, eso no es un numero. Ingrese el precio del cual desea calcular el (5%) de aumento: ")) # Si el usuario no ingresa un numero le pide denuevo

precio_con_aumento = aplicarAumento(precio_ingresado) # Llamo a la funcion y le pongo valor a lo que devuelve para despues mostrarlo

print(f"El precio final con el aumento del 5% es: ${precio_con_aumento}")