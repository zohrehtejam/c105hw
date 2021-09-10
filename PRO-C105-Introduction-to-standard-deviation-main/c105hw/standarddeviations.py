import pandas as pd
import statistics
import math

data = [60,61,65,63,98,99,90,95,91,96]

#Many lines difficult code
mean = statistics.mean(data)

deviations = []

for i in data:
    dif = i-mean 
    deviations.append(dif)

squared_deviations = []

for i in deviations:
    s = i* i
    squared_deviations.append(s)

sum_squared_deviations = 0

for i in squared_deviations:
    sum_squared_deviations = i + sum_squared_deviations
    
number_of_data = len(data)

variance = sum_squared_deviations/number_of_data

standard_deviation = math.sqrt(variance)

print("The standarad deviation: ", standard_deviation )

#Standard deviations one line code
result = statistics.stdev(data)
print(result)

