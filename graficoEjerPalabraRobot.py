import random
import string
import matplotlib.pyplot as plt

# Palabra objetivo y parámetros del Algoritmo Genético
TARGET = "ROBOT"
GENES = string.ascii_uppercase  # Alfabeto 'A-Z'
POP_SIZE = 12                   # Tamaño de la población
MUTATION_RATE = 0.1             # Probabilidad de mutación por letra

# 1. Función de Fitness
def calculate_fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET) if a == b)

def create_individual():
    return "".join(random.choice(GENES) for _ in range(len(TARGET)))

# Población inicial
population = [create_individual() for _ in range(POP_SIZE)]

# Listas para guardar el historial de métricas para la gráfica
history_max = []
history_avg = []
generations_list = []

generation = 1
while True:
    # Evaluar fitness
    scores = [calculate_fitness(ind) for ind in population]
    
    # Calcular métricas de la generación actual
    max_fit = max(scores)
    avg_fit = sum(scores) / len(scores)
    
    history_max.append(max_fit)
    history_avg.append(avg_fit)
    generations_list.append(generation)
    
    # Ordenar población de mayor a menor fitness
    ranked_pop = [ind for ind, _ in sorted(zip(population, scores), key=lambda x: x[1], reverse=True)]
    best_ind = ranked_pop[0]
    
    print(f"Gen {generation:2d} | Mejor: {best_ind} | Fitness Max: {max_fit}/{len(TARGET)} | Promedio: {avg_fit:.2f}")
    
    # Condición de parada
    if max_fit == len(TARGET):
        print(f"\n¡Éxito! Palabra '{TARGET}' alcanzada en la generación {generation}.")
        break
        
    # Selección con Elitismo (conservamos los 2 mejores)
    new_population = ranked_pop[:2]
    
    # Reproducción
    while len(new_population) < POP_SIZE:
        # Selección de padres entre los mejores
        p1, p2 = random.sample(ranked_pop[:6], 2)
        
        # Crossover (Punto de corte aleatorio)
        crossover_point = random.randint(1, len(TARGET) - 1)
        child = p1[:crossover_point] + p2[crossover_point:]
        
        # Mutación
        child_mutated = []
        for char in child:
            if random.random() < MUTATION_RATE:
                child_mutated.append(random.choice(GENES))
            else:
                child_mutated.append(char)
        child = "".join(child_mutated)
        
        new_population.append(child)
        
    population = new_population
    generation += 1

# =========================================================
# GRAFICAR RESULTADOS CON MATPLOTLIB
# =========================================================
plt.figure(figsize=(9, 5))

# Dibujar la curva del fitness máximo y promedio
plt.plot(generations_list, history_max, marker='o', color='green', linewidth=2, label='Fitness Máximo (Mejor Individuo)')
plt.plot(generations_list, history_avg, marker='s', color='orange', linestyle='--', label='Fitness Promedio de la Población')

# Línea de meta (Fitness perfecto = 5)
plt.axhline(y=len(TARGET), color='red', linestyle=':', label=f'Meta (Target: "{TARGET}")')

# Configuración del gráfico
plt.title('Evolución del Algoritmo Genético hacia la palabra "ROBOT"', fontsize=13, fontweight='bold')
plt.xlabel('Generación', fontsize=11)
plt.ylabel('Fitness (Coincidencias de letras)', fontsize=11)
plt.yticks(range(0, len(TARGET) + 1))
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right')

# Ajustar y mostrar
plt.tight_layout()
plt.show()