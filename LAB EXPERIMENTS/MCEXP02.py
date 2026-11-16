import matplotlib.pyplot as plt

cells = [(0, 0), (1, 0), (0, 1), (-1, 1),
         (-1, 0), (0, -1), (1, -1)]

colors = ['red', 'blue', 'green', 'yellow',
          'orange', 'purple', 'cyan']

for i, (x, y) in enumerate(cells):
    plt.scatter(x, y, s=2000, color=colors[i], alpha=0.4)
    plt.text(x, y, "Cell " + str(i+1), ha='center')

plt.title("Cellular Layout and Frequency Reuse")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid()
plt.show()
