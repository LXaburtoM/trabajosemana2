Algoritmo Ejercicio_3_matriz
	Definir monto, tasa_interes, años, monto_final Como Real
	
	Escribir "Ingrese el monto del préstamo: "
	Leer monto
	
	tasa_interes = 0.03
	años = 5
	monto_final = monto * (1 + tasa_interes) ^ años
	Escribir "El monto total a pagar después de 5 años es: ", monto_final
FinAlgoritmo
