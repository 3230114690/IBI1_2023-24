#take the amount of cell as a variable called A
A=0.05
#consider integer "day" as another variable
day=1
#use while to solve the problem
while A<=0.9:
     A=A*2
     day=day+1
print("On day "+str(day)+", the cell density reaches the target, and the number of day is my maximum rest time"  )