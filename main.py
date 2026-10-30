# ===== DATOS: 5 listas de 25 elementos (paciente Nº1 = índice 0) =====
nombres = ["Ana","Luis","Camila","Jorge","Sofía","Andrés","Valentina","Pedro","María","Carlos","Laura","Diego","Elena","Fernando","Gabriela","Hugo","Isabel","Javier","Karla","Leonardo","Mónica","Nicolás","Olivia","Pablo","Renata"]  # nombres de los pacientes
edades = [28,35,22,41,30,25,38,29,33,27,45,24,31,36,26,42,23,34,29,37,21,32,39,26,44]  # edades de los pacientes
temperaturas = [36.5,38.2,37.0,39.1,36.8,38.5,36.9,37.5,38.0,36.6,37.8,39.5,36.7,38.3,37.2,38.8,36.4,39.0,37.6,36.9,38.4,37.1,39.2,36.5,38.6]  # temperaturas en °C
obras_sociales = [True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True]  # True si tiene obra social
riesgos = [88,72,91,65,78,55,94,82,76,85,70,92,68,79,95,62,87,74,90,66,93,77,81,89,63]  # nivel de riesgo

# Producto 0
print("=== PRODUCTO 0 ===")  # título de la sección
print("El paciente 5 se llama", nombres[4], ", tiene", edades[4], "años y su temperatura es", temperaturas[4], "°C.")  # imprime los datos de Sofía

# Producto 1 Parte A
def tiene_obra_social(obra):  # predicado P(x): tiene obra social
    return obra == True  # True si la obra social es True

def tiene_fiebre(temp):  # predicado Q(x): tiene fiebre
    return temp >= 38.0  # True si la temperatura es 38.0 o más

def riesgo_alto(riesgo):  # predicado R(x): riesgo alto
    return riesgo >= 80  # True si el riesgo es 80 o más

def es_adulto_mayor(edad):  # predicado S(x): adulto mayor
    return edad >= 40  # True si la edad es 40 o más

# Producto 1 Parte B
print("\n=== PRODUCTO 1 - AFIRMACIÓN 1 (∀x (¬P(x) → Q(x))) ===")  # título de la sección
afirmacion1 = True  # supone verdadera hasta encontrar un contraejemplo
contraejemplos = []  # lista de contraejemplos
for i in range(25):  # recorre los 25 pacientes
    if not tiene_obra_social(obras_sociales[i]):  # Pregunta si NO tiene obra social (antecedente verdadero)
        if not tiene_fiebre(temperaturas[i]):  # y si NO tiene fiebre (consecuente falso)
            afirmacion1 = False  # la implicación falla, la afirmación es falsa
            contraejemplos.append(nombres[i])  # guarda el contraejemplo
print("Podemos decir que la Afirmación 1 es: ", afirmacion1)  # imprime el veredicto
print("Contraejemplos:", contraejemplos)  # imprime los contraejemplos

print("\n=== PRODUCTO 1 - AFIRMACIÓN 2 (∃x (R(x) ∧ S(x))) ===")  # título de la sección
afirmacion2 = False  # supone falsa hasta encontrar un testigo
testigos = []  # lista de testigos
for i in range(25):  # recorre los 25 pacientes
    if riesgo_alto(riesgos[i]) and es_adulto_mayor(edades[i]):  # riesgo alto Y adulto mayor
        afirmacion2 = True  # encontró un testigo, entonces la existencia se cumple
        testigos.append(nombres[i])  # guarda el testigo
print("Podemos decir que la Afirmación 2 es: ", afirmacion2)  # imprime el veredicto
print("Testigos:", testigos)  # imprime los testigos

# Producto 2, Leyes de Morgan
print("\n=== PRODUCTO 2 - DE MORGAN ===")  # título de la sección

# Ley 1: ¬(∀x P(x)) ≡ ∃x ¬P(x)
todos_con_obra = True  # ∀x P(x): supone que todos tienen obra social
for i in range(25):  # recorre los 25 pacientes
    if not tiene_obra_social(obras_sociales[i]):  # si alguien no tiene obra social
        todos_con_obra = False  # ∀x P(x) es falsa
lado1_izq = not todos_con_obra  # lado izquierdo: ¬(∀x P(x))

##############################################################################

existe_sin_obra = False  # ∃x ¬P(x): supone que nadie carece de obra social
for i in range(25):  # recorre los 25 pacientes
    if not tiene_obra_social(obras_sociales[i]):  # si alguien no tiene obra social
        existe_sin_obra = True  # ∃x ¬P(x) es verdadera
lado1_der = existe_sin_obra  # lado derecho: ∃x ¬P(x)
print("Ley 1 -> izquierda:", lado1_izq, "| derecha:", lado1_der, "| equivalentes:", lado1_izq == lado1_der)  # compara ambos lados

# Ley 2: ¬(∃x Q'(x)) ≡ ∀x ¬Q'(x), con Q'(x): temp >= 39.5
existe_temp = False  # ∃x (temp >= 39.5): supone que nadie llega a 39.5
for i in range(25):  # recorre los 25 pacientes
    if temperaturas[i] >= 39.5:  # si alguien tiene 39.5 o más
        existe_temp = True  # ∃x Q'(x) es verdadera
lado2_izq = not existe_temp  # lado izquierdo: ¬(∃x Q'(x))

###############################################################################

todos_menor = True  # ∀x (temp < 39.5): supone que todos están por debajo
for i in range(25):  # recorre los 25 pacientes
    if not (temperaturas[i] < 39.5):  # si alguien no está por debajo de 39.5
        todos_menor = False  # ∀x ¬Q'(x) es falsa
lado2_der = todos_menor  # lado derecho: ∀x ¬Q'(x)
print("Ley 2 -> izquierda:", lado2_izq, "| derecha:", lado2_der, "| equivalentes:", lado2_izq == lado2_der)  # compara ambos lados

# Producto 3, verificar paciente 
def verificar_paciente(nombre, edad, temperatura, obra_social, riesgo):
    # Comprobamos que no tenga obra social, tenga fiebre y no tenga riesgo alto
    if obra_social == False and temperatura >= 38.0 and riesgo < 80:
        # Devolvemos True si cumple las tres condiciones
        return True
    else:
        # Devolvemos False si no cumple alguna condición
        return False
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
# Definimos una función para verificar las condiciones del paciente
 
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