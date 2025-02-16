# Lista vacía donde guardaremos los números
numeros = []

# Bucle que pide números hasta que el usuario escriba 'listo'
while True:
    entrada = input("Introduce un número (o escribe 'listo' para terminar): ")
    
    if entrada.strip().lower() == 'listo':  # Si el usuario escribe 'listo', terminamos el bucle
        break
    
    # Convertir la entrada a un número entero
    try:
        numero = int(entrada) # Usando int() para convertir a entero
        numeros.append(numero) # Agregar el número a la lista
    except ValueError:
        print("Por favor, introduce un número válido.") #Si la entrada no es un número, avisamos al usuario

# Mostrar los números ingresados
print("Números ingresados:", numeros)

# Calcular el promedio si la lista no está vacía
if len(numeros) > 0:
    promedio = round(sum(numeros)/len(numeros),2)
    print("El promedio es: ", promedio)
else:
    print("No se ingresaron números.")