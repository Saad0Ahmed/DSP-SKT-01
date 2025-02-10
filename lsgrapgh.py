import matplotlib.pyplot as plt
import numpy as np
n = np.linspace (1,50,50)
best_case = np.ones_like(n)
average_case = n
worst_case = n
plt.figure ( figsize=(10,20) )
plt.plot(n, best_case,label="Best_case:0(1)",color="green",linewidth=2 )
plt.plot(n,average_case,label="Average_case:o(n)",c="red",linewidth=2,linestyle="--")
plt.plot(n,worst_case,label="Worst_case:0(n)",c="blue",linestyle=":",linewidth=2)
plt.xlabel("Input size(n)" , fontsize=14)
plt.ylabel("Time complexity ", fontsize=14)
plt.title("Grph for time complexity of Linear search ")
plt.grid(True)
plt.legend()
plt.show()