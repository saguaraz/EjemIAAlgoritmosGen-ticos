import random
import matplotlib.pyplot as plt
import numpy as np

# Función a maximizar
def fitness(x):
    return x ** 2

# Parámetros del AG
pop_size = 10
generations = 10
mutation_rate = 0.2

# Población inicial
population = [random.uniform(-10, 10) for _ in range(pop_size)]

# Preparar gráfico
fig, ax = plt.subplots(figsize=(8, 5))
x_func = np.linspace(-10, 10, 400)
y_func = fitness(x_func)

# Guardar historial para graficar
history = []

for gen in range(generations):
    scores = [fitness(x) for x in population]
    history.append((population.copy(), scores.copy()))
    
    # Selección de los 2 mejores
    parents = sorted(zip(population, scores), key=lambda item: item[1], reverse=True)[:2]
    p1, p2 = parents[0][0], parents[1][0]
    
    # Cruzamiento y Mutación
    child = (p1 + p2) / 2
    if random.random() < mutation_rate:
        child += random.uniform(-1, 1)
        child = max(-10, min(10, child))
        
    population = [p1, p2, child] + [random.uniform(-10, 10) for _ in range(pop_size - 3)]

# Graficar curva base f(x) = x²
ax.plot(x_func, y_func, label="f(x) = x²", color="blue", linewidth=2)

# Graficar individuos de la primera y última generación
first_pop, first_scores = history[0]
last_pop, last_scores = history[-1]

ax.scatter(first_pop, first_scores, color="red", label="Población Inicial (Gen 1)", zorder=5, s=60)
ax.scatter(last_pop, last_scores, color="green", label=f"Población Final (Gen {generations})", zorder=5, s=60)

ax.set_title("Evolución del Algoritmo Genético en f(x) = x²")
ax.set_xlabel("x")
ax.set_ylabel("Fitness f(x)")
ax.legend()
ax.grid(True)

plt.show()