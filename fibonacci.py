import matplotlib.pyplot as plt

n = 20
fib = [0,1]

for i in range(2,n):
    fib.append(fib[i-1] + fib[i-2])

plt.figure(figsize=(10,5))
plt.plot(range(n), fib, marker = 'o', linestyle = '-', color = 'b', label = "Fibonacci Sequence")

plt.xlabel("Index (n)")
plt.ylabel("Fibonacci Value")
plt.title(f"Fibonacci Sequence (first {n} Terms")
plt.legend()
plt.grid(True)
plt.show()