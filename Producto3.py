

# Definimos una función para verificar las condiciones del paciente
def verificar_paciente(nombre, edad, temperatura, obra_social, riesgo):
    # Comprobamos que no tenga obra social, tenga fiebre y no tenga riesgo alto
    if obra_social == False and temperatura >= 38.0 and riesgo < 80:
        # Devolvemos True si cumple las tres condiciones
        return True
    else:
        # Devolvemos False si no cumple alguna condición
        return False

# Probamos la función con los datos del paciente Luis
resultado = verificar_paciente("Luis", 35, 38.2, False, 72)

# Mostramos el resultado en pantalla
print(resultado)

# Guardamos los nombres de los 25 pacientes
nombres = ["Ana", "Luis", "Camila", "Jorge", "Sofía", "Andrés", "Valentina", "Pedro", "María", "Carlos", "Laura", "Diego", "Elena", "Fernando", "Gabriela", "Hugo", "Isabel", "Javier", "Karla", "Leonardo", "Mónica", "Nicolás", "Olivia", "Pablo", "Renata"]

# Guardamos las edades de los pacientes
edades = [28, 35, 22, 41, 30, 25, 38, 29, 33, 27, 45, 24, 31, 36, 26, 42, 23, 34, 29, 37, 21, 32, 39, 26, 44]

# Guardamos las temperaturas de los pacientes
temperaturas = [36.5, 38.2, 37.0, 39.1, 36.8, 38.5, 36.9, 37.5, 38.0, 36.6, 37.8, 39.5, 36.7, 38.3, 37.2, 38.8, 36.4, 39.0, 37.6, 36.9, 38.4, 37.1, 39.2, 36.5, 38.6]

# Indicamos si cada paciente tiene obra social
obras_sociales = [True, False, True, True, False, False, True, False, True, True, True, False, True, False, True, True, False, True, False, True, False, True, False, True, True]

# Guardamos el nivel de riesgo de cada paciente
riesgos = [88, 72, 91, 65, 78, 55, 94, 82, 76, 85, 70, 92, 68, 79, 95, 62, 87, 74, 90, 66, 93, 77, 81, 89, 63]

# Mostramos la cantidad de pacientes registrados
print("Pacientes registrados:", len(nombres))

# Creamos una lista para los pacientes que cumplen la condición
cumplen = []

# Creamos una lista para los pacientes que no cumplen la condición
no_cumplen = []

# Recorremos las posiciones de los 25 pacientes
for i in range(25):
    # Verificamos las condiciones usando los datos de cada paciente
    resultado = verificar_paciente(nombres[i], edades[i], temperaturas[i], obras_sociales[i], riesgos[i])

    # Si el paciente cumple las condiciones, guardamos su nombre
    if resultado == True:
        cumplen.append(nombres[i])
    else:
        # Si no cumple, guardamos su nombre en la otra lista
        no_cumplen.append(nombres[i])

# Mostramos los pacientes que cumplen
print("Pacientes que cumplen:", cumplen)

# Mostramos la cantidad de pacientes que cumplen
print("Cantidad que cumplen:", len(cumplen))

# Mostramos los pacientes que no cumplen
print("Pacientes que no cumplen:", no_cumplen)

# Mostramos la cantidad de pacientes que no cumplen
print("Cantidad que no cumplen:", len(no_cumplen))

# Recorremos los 25 pacientes para mostrar los datos de quienes cumplen
for i in range(25):
    # Verificamos nuevamente las condiciones de cada paciente
    if verificar_paciente(nombres[i], edades[i], temperaturas[i], obras_sociales[i], riesgos[i]) == True:
        # Mostramos el nombre del paciente
        print("Nombre:", nombres[i])
        # Mostramos la edad del paciente
        print("Edad:", edades[i])
        # Mostramos su temperatura
        print("Temperatura:", temperaturas[i], "°C")
        # Mostramos si tiene obra social
        print("Tiene obra social:", obras_sociales[i])
        # Mostramos su nivel de riesgo
        print("Riesgo:", riesgos[i])
        # Separamos los datos de cada paciente
        print("--------------------")