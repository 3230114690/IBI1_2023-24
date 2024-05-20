# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define a function to run the SIR model with vaccination
def run_SIR_model(vaccination_rate):
    # Define basic variables
    N = 10000  # Total population
    V = int(N * vaccination_rate)  # Initial number of vaccinated individuals
    S = N - V - 1  # Initial number of susceptible individuals
    I = 1  # Initial number of infected individuals
    R = 0  # Initial number of recovered individuals

    beta = 0.3  # Infection rate
    gamma = 0.05  # Recovery rate

    # Arrays to track the numbers of Susceptible, Infected, Recovered, and Vaccinated individuals over time
    S_array = [S]
    I_array = [I]
    R_array = [R]
    V_array = [V]

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
        V_array.append(V)

    return S_array, I_array, R_array, V_array

# Plot results for different vaccination rates
vaccination_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]  # Different vaccination percentages
plt.figure(figsize=(10, 6), dpi=150)

for rate in vaccination_rates:
    S_array, I_array, R_array, V_array = run_SIR_model(rate)
    plt.plot(I_array, label=f'Vaccination rate = {rate*100:.0f}%', color=cm.viridis(rate*256))

plt.xlabel('Time')
plt.ylabel('Number of Infected Individuals')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.savefig('SIR_vaccination_model.png')
plt.show()
