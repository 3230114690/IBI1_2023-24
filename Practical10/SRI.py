# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define basic variables
N = 10000  # Total population
S = 9999  # Initial number of susceptible individuals
I = 1  # Initial number of infected individuals
R = 0  # Initial number of recovered individuals

beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Arrays to track the numbers of Susceptible, Infected, and Recovered individuals over time
S_array = [S]
I_array = [I]
R_array = [R]

# Time points
time_points = 1000

# Time loop
for t in range(time_points):
    # Probability of infection and recovery
    prob_infection = beta * I / N
    prob_recovery = gamma
    
    # Calculate new infections and recoveries
    new_infections = np.random.choice([0, 1], S, p=[1 - prob_infection, prob_infection]).sum()
    new_recoveries = np.random.choice([0, 1], I, p=[1 - prob_recovery, prob_recovery]).sum()
    
    # Update numbers
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    
    # Record the updated numbers
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

# Plot results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_array, label='Susceptible')
plt.plot(I_array, label='Infected')
plt.plot(R_array, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of Individuals')
plt.title('SIR Model')
plt.legend()
plt.savefig('SIR_model.png')
plt.show()
