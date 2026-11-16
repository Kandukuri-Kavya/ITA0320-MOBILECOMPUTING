import matplotlib.pyplot as plt
import random

time = list(range(1, 11))
throughput = [random.randint(10, 100) for i in time]

plt.plot(time, throughput, marker='o')

plt.title("Network Throughput")
plt.xlabel("Time")
plt.ylabel("Throughput (Mbps)")

plt.grid()
plt.show()
