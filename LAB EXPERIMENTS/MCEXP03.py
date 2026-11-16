position = 0

for time in range(1, 11):
    position += 1

    if position <= 3:
        cell = "Cell 1"
    elif position <= 6:
        cell = "Cell 2"
    else:
        cell = "Cell 3"

    print("Time:", time, "Position:", position,
          "Connected to:", cell)
