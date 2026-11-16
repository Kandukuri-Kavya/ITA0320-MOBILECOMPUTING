import matplotlib.pyplot as plt
import random

time = list(range(1, 11))
latency = [random.randint(10, 100) for i in time]

plt.plot(time, latency, marker='o')

plt.title("Mobile Network Latency")
plt.xlabel("Time")
plt.ylabel("Latency (ms)")

plt.grid()
plt.show()
