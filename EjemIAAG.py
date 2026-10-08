import random
# Función para inicializar la población
def inicializar_poblacion(tamano_poblacion, longitud_individuo):
    poblacion = []
    for _ in range(tamano_poblacion):
        individuo = [random.randint(0 , 1) for _ in range(longitud_individuo)]
        poblacion.append(individuo)
    return poblacion

# Función para evaluar la aptitud de un individuo
def evaluar_aptitud(individuo):
    # Implementar la función de evaluación específica del problema
    # Aquí, asumimos que la aptitud es la suma de los valores de los genes (para ilustrar)
    return sum(individuo)

# Función para seleccionar padres usando selección por torneo
def seleccion_torneo(poblacion, k):
    mejor_individuo = random.choice(poblacion)
    for _ in range(k - 1):
        individuo = random.choice(poblacion)
        if evaluar_aptitud(individuo) > evaluar_aptitud(mejor_individuo):
            mejor_individuo = individuo
    return mejor_individuo

# Función para cruzar dos padres y generar un hijo
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 2)
    hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
    return hijo

# Función para mutar un individuo
def mutacion(individuo, tasa_mutacion):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo[i] = 1 - individuo[i]  # Cambiar de 0 a 1 o de 1 a 0
    return individuo
def algoritmo_genetico():
    tamano_poblacion = 100
    longitud_individuo = 10
    numero_generaciones = 50
    tasa_mutacion = 0.01
    k = 5  # Tamaño del torneo

    # Inicializar población
    poblacion = inicializar_poblacion(tamano_poblacion, longitud_individuo)

    # Evolucionar la población
    for generacion in range(numero_generaciones):
        nueva_poblacion = []

        # Evaluar aptitud de cada individuo
        aptitudes = [evaluar_aptitud(individuo) for individuo in poblacion]

        # Generar nueva población
        for _ in range(tamano_poblacion):
            # Selección
            padre1 = seleccion_torneo(poblacion, k)
            padre2 = seleccion_torneo(poblacion, k)

            # Cruce
            hijo = cruce(padre1, padre2)

            # Mutación
            hijo = mutacion(hijo, tasa_mutacion)

            nueva_poblacion.append(hijo)

        # Reemplazar la población antigua con la nueva
        poblacion = nueva_poblacion

    # Encontrar el mejor individuo de la última generación
    mejor_individuo = poblacion[0]
    mejor_aptitud = evaluar_aptitud(mejor_individuo)
    for individuo in poblacion:
        aptitud = evaluar_aptitud(individuo)
        if aptitud > mejor_aptitud:
            mejor_individuo = individuo
            mejor_aptitud = aptitud
    print("El mejor individuo es:", mejor_individuo)
    print("Con una aptitud de:", mejor_aptitud)

    print("Población final:")
    for individuo in poblacion:
        print(individuo, "Aptitud:", evaluar_aptitud(individuo))

if __name__ == "__main__":
    algoritmo_genetico()
