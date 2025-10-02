import numpy as np
import matplotlib.pyplot as plt
import os

os.system("clear")

a = np.arange(6)

print(f"Before reshape\n {a}\n")

res_a = a.reshape(2, 3)

print(f"After reshape\n {res_a}\n")

data = np.random.normal(loc=50, scale=10, size=1000) 
#loc is the mean, scale is the standard deviation, size is the number of samples
mean = np.mean(data)

std_dev = np.std(data)

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")

#plot a histogram
plt.hist(data, bins=30, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()