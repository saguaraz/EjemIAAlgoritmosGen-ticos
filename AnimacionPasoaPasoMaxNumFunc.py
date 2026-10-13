import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def fitness(x): return x ** 2

pop_size = 10
generations = 15
mutation_rate = 0.2
population = [random.uniform(-10, 10) for _ in range(pop_size)]

history = []
for gen in range(generations):
    scores = [fitness(x) for x in population]
    history.append(list(zip(population, scores)))
    
    parents = sorted(zip(population, scores), key=lambda item: item[1], reverse=True)[:2]
    p1, p2 = parents[0][0], parents[1][0]
    child = (p1 + p2) / 2
    if random.random() < mutation_rate:
        child = max(-10, min(10, child + random.uniform(-1, 1)))
    population = [p1, p2, child] + [random.uniform(-10, 10) for _ in range(pop_size - 3)]

fig, ax = plt.subplots(figsize=(8, 5))
x_curve = np.linspace(-10, 10, 300)
ax.plot(x_curve, fitness(x_curve), 'b-', alpha=0.6, label='f(x) = x²')
scat = ax.scatter([], [], c='red', s=70, zorder=5, label='Individuos')
title = ax.set_title('')

def update(frame):
    data = history[frame]
    xs = [d[0] for d in data]
    ys = [d[1] for d in data]
    scat.set_offsets(np.c_[xs, ys])
    title.set_text(f'Generación {frame + 1} / {generations}')
    return scat, title

ani = animation.FuncAnimation(fig, update, frames=len(history), interval=600, blit=True)
plt.xlabel('x')
plt.ylabel('Fitness')
plt.legend()
plt.grid(True)
plt.show()