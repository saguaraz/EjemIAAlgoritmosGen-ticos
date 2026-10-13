import random

# Función a maximizar
def fitness(x):
    return x ** 2

# Parámetros del Algoritmo Genético
pop_size = 6
generations = 10
mutation_rate = 0.3  # Aumentado levemente para ver más mutaciones

# Población inicial en el rango [-10, 10]
population = [random.uniform(-10, 10) for _ in range(pop_size)]

print("=== INICIO DEL ALGORITMO GENÉTICO ===")
for gen in range(generations):
    # 1. Evaluar fitness de la población actual
    scores = [fitness(x) for x in population]
    
    # 2. Selección: Elegir a los 2 mejores padres
    parents = sorted(zip(population, scores), key=lambda x: x[1], reverse=True)[:2]
    p1, p2 = parents[0][0], parents[1][0]
    
    # 3. Cruzamiento (Crossover): Promedio de los padres
    child = (p1 + p2) / 2
    
    # 4. Mutación: Pequeña variación aleatoria
    if random.random() < mutation_rate:
        child += random.uniform(-1, 1)
        # Asegurar que el hijo se mantenga dentro del rango [-10, 10]
        child = max(-10, min(10, child))
    
    # 5. Nueva generación: Se conservan los 2 mejores padres, el hijo y se generan nuevos aleatorios
    population = [p1, p2, child] + [random.uniform(-10, 10) for _ in range(pop_size - 3)]
    
    # Obtener el mejor de la generación actual
    best = max(population, key=fitness)
    print(f"Generación {gen + 1:2d} | Mejor individuo x: {best:7.3f} | Fitness (x²): {fitness(best):7.3f}")

print("\n=== RESULTADO FINAL ===")
best_final = max(population, key=fitness)
print(f"El valor de x que maximiza f(x) encontrado es: {best_final:.3f}")
print(f"Fitness alcanzado: {fitness(best_final):.3f}")