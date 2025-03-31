import math

def area_circulo():
    # Solicitar el radio del círculo
    radio = float(input("Introduce el radio del círculo: "))
    area = math.pi * (radio ** 2)
    # Mostrar el resultado
    print("El área del círculo con radio", radio, "es:", area)
# Llamar a la función para ejecutar el cálculo del área
area_circulo()