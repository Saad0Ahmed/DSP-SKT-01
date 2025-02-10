import matplotlib.pyplot as plt
import numpy as np
n = np.linspace (1,50,50)
best_case = n
average_case = n**2
worst_case = n**2
plt.figure ( figsize=(10,20) )
plt.plot(n, best_case,label="Best_case:0(n)",color="green",linewidth=2 )
plt.plot(n,average_case,label="Average_case:o(n**2)",c="red",linewidth=2,linestyle="--")
plt.plot(n,worst_case,label="Worst_case:0(n**2)",c="blue",linestyle=":",linewidth=2)
plt.xlabel("Input size(n)" , fontsize=14)
plt.ylabel("Time complexity ", fontsize=14)
plt.title("Grph for time complexity of Bubble sort ")
plt.grid(True)
plt.legend()
plt.show()