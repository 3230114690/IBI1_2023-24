# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Initialize model parameters
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
grid_size = 100  # Size of the grid

# Create a grid with all individuals initially susceptible
population = np.zeros((grid_size, grid_size))

# Infect one random individual
outbreak = np.random.choice(range(grid_size), 2)
population[outbreak[0], outbreak[1]] = 1

# Function to plot the population
def plot_population(population, time_step):
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time step: {time_step}')
    plt.colorbar(label='State')
    plt.show()

# Plot the initial state
plot_population(population, 0)

# Function to get the neighbors of a cell
def get_neighbors(x, y, grid_size):
    neighbors = []
    for i in range(max(0, x-1), min(grid_size, x+2)):
        for j in range(max(0, y-1), min(grid_size, y+2)):
            if (i, j) != (x, y):
                neighbors.append((i, j))
    return neighbors

# Time course simulation
time_points = 100
for t in range(1, time_points + 1):
    new_population = np.copy(population)
    
    # Find infected points
    infected_indices = np.argwhere(population == 1)
    
    # Process each infected individual
    for (i, j) in infected_indices:
        # Infect susceptible neighbors
        for (ni, nj) in get_neighbors(i, j, grid_size):
            if population[ni, nj] == 0 and np.random.rand() < beta:
                new_population[ni, nj] = 1
        
        # Recover the infected individual with probability gamma
        if np.random.rand() < gamma:
            new_population[i, j] = 2
    
    population = new_population

    # Plot the population at specific time points
    if t in [0, 10, 50, 100]:
        plot_population(population, t)
