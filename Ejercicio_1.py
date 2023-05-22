def aplicarAumento(precio: float):
    aumento = precio * 0.05

    precio_con_aumento = precio + aumento
    return precio_con_aumento


precio_ingresado = int(input("Ingrese el precio del cual desea calcular el (5%) de aumento: "))

precio_con_aumento = aplicarAumento(precio_ingresado)

print(f"El precio final con el aumento del 5% es: ${precio_con_aumento}")