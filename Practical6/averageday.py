import matplotlib.pyplot as plt
#Use the original data
time = {
    'Sleeping': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1,
    'Others':3.5
}
total_hours = 24
# Calculate hours spent on 'other'
hours_spent_on_activities = sum(time.values())
hours_spent_on_other = total_hours - hours_spent_on_activities
print(time)
print()
#pie chart
activities = list(time.keys())
time_spent = list(time.values())
#plotting the chart
plt.figure()
plt.pie(time_spent, labels=activities,startangle=90)
plt.title('Average Day of a University Student')
plt.show()
plt.clf()