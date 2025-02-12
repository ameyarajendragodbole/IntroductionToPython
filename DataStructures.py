import numpy
from matplotlib import pyplot as plt

print("Hello World!")
print("line 2")
print("line 3")

arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

x_values = [1, 2, 3, 4]
y_values = [5, 4, 6, 2]

plt.plot(x_values, y_values)
plt.savefig("plot.png", dpi=300)

