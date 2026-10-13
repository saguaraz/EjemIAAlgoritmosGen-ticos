import random
import string

# Palabra objetivo y constantes
TARGET = "ROBOT"
GENES = string.ascii_uppercase  # Alfabeto en mayúsculas 'A-Z'
POP_SIZE = 10                  # Tamaño de la población
MUTATION_RATE = 0.1            # Probabilidad de mutación por letra

# 1. Función de Aptitud (Fitness)
# Cuenta cuántas letras coinciden exactamente en letra y posición con TARGET
def calculate_fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET) if a == b)

# Genera un individuo aleatorio de 5 letras
def create_individual():
    return "".join(random.choice(GENES) for _ in range(len(TARGET)))

# 2. Población inicial
population = [create_individual() for _ in range(POP_SIZE)]

print(f"=== INICIO DE BÚSQUEDA DEL TARGET: '{TARGET}' ===")

generation = 1
while True:
    # Evaluar el fitness de toda la población
    scores = [calculate_fitness(ind) for ind in population]
    
    # Ordenar la población de mayor a menor fitness
    ranked_pop = [ind for ind, _ in sorted(zip(population, scores), key=lambda x: x[1], reverse=True)]
    best_ind = ranked_pop[0]
    best_fitness = calculate_fitness(best_ind)
    
    print(f"Generación {generation:3d} | Mejor: {best_ind} | Fitness: {best_fitness}/{len(TARGET)}")
    
    # Criterio de parada: ¿Se encontró la palabra objetivo?
    if best_fitness == len(TARGET):
        print(f"\n¡Éxito! Palabra '{TARGET}' alcanzada en la generación {generation}.")
        break
        
    # 3. Selección: Elegimos a los mejores (Elitismo)
    # Conservamos los 2 mejores directamente para la siguiente generación
    new_population = ranked_pop[:2]
    
    # 4. Generar hijos mediante Cruzamiento y Mutación para completar la población
    while len(new_population) < POP_SIZE:
        # Selección de 2 padres entre los mejores individuos de la generación actual
        p1, p2 = random.sample(ranked_pop[:5], 2)
        
        # Cruzamiento (Crossover de un punto)
        crossover_point = random.randint(1, len(TARGET) - 1)
        child = p1[:crossover_point] + p2[crossover_point:]
        
        # Mutación
        child_mutated = []
        for char in child:
            if random.random() < MUTATION_RATE:
                child_mutated.append(random.choice(GENES))  # Cambia por una letra aleatoria
            else:
                child_mutated.append(char)
        child = "".join(child_mutated)
        
        new_population.append(child)
        
    population = new_population
    generation += 1