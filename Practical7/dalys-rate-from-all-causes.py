import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("\\Users\\29284\\Desktop\\IBI1\\IBI1_2023-24\\Practical7")
current_directory = os.getcwd()
print("\\Users\\29284\\Desktop\\IBI1\\IBI1_2023-24\\Practical7", current_directory)
files_in_directory = os.listdir()
print("\\Users\\29284\\Desktop\\IBI1\\IBI1_2023-24\\Practical7:", files_in_directory)
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head())
dalys_data.head(5)
dalys_data.info()

my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3, my_columns])

print(dalys_data.loc[:, "Entity"])

is_afghanistan = dalys_data["Entity"] == "Afghanistan"
print(dalys_data.loc[is_afghanistan, "DALYs"])

import numpy as np
import matplotlib.pyplot as plt

china_data = dalys_data.loc[dalys_data["Entity"] == "China", ["Entity", "Year", "DALYs"]]

# calculate
mean_dalys_china = np.mean(china_data["DALYs"])
print("Mean DALYs in China over time:", mean_dalys_china)

# make comparison
daly_2019 = china_data.loc[china_data["Year"] == 2019, "DALYs"].values[0]
if daly_2019 > mean_dalys_china:
    print("DALYs in 2019 is above the mean.")
elif daly_2019 < mean_dalys_china:
    print("DALYs in 2019 is below the mean.")
else:
    print("DALYs in 2019 is equal to the mean.")

#print the plot
plt.plot(china_data["Year"], china_data["DALYs"], 'b+')  
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in China over Time")
plt.xticks(china_data["Year"], rotation=-90) 
plt.grid(True)  
plt.show()

#Plot a boxplot of DALYs across countries in 2019.
year_2019_data = dalys_data[dalys_data["Year"] == 2019]
plt.figure(figsize=(10, 6))
plt.boxplot(year_2019_data["DALYs"], vert=False)
plt.xlabel("DALYs")
plt.title("Boxplot of DALYs across Countries in 2019")
plt.grid(True)
plt.show()
