import matplotlib.pyplot as plt  

# creat a dictionary
cities = [
    {"name": "Edinburgh", "country": "UK", "population": 0.56},
    {"name": "Glasgow", "country": "UK", "population": 0.62},
    {"name": "Stirling", "country": "UK", "population": 0.04},
    {"name": "London", "country": "UK", "population": 9.7},
    {"name": "Haining", "country": "China", "population": 0.58},
    {"name": "Hangzhou", "country": "China", "population": 8.4},
    {"name": "Shanghai", "country": "China", "population": 29.9},
    {"name": "Beijing", "country": "China", "population": 22.2}
]
# divide the data according to the countries
uk_populations = [city["population"] for city in cities if city["country"] == "UK"]
china_populations = [city["population"] for city in cities if city["country"] == "China"]
uk_populations.sort()
china_populations.sort()
# plot the chart
plt.figure(figsize=(12, 6)) 
# design the size
plt.subplot(1, 2, 1) 
plt.bar(range(len(uk_populations)), uk_populations, color='skyblue')  
# create the chart
plt.title('population of UK')  
plt.xlabel('city')  
plt.ylabel('population(million)') 
plt.xticks(range(len(uk_populations)), [city["name"] for city in cities if city["country"] == "UK"], rotation=45) 
plt.subplot(1, 2, 2) 
#second one
plt.bar(range(len(china_populations)), china_populations, color='lightgreen') 
 # create the chart, set lables and other things
plt.title('population of China')  
plt.xlabel('city') 
plt.ylabel('population(million)') 
plt.xticks(range(len(china_populations)), [city["name"] for city in cities if city["country"] == "China"], rotation=45) 
plt.show() 