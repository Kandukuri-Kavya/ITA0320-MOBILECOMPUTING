import random

for i in range(1, 6):
    signal = random.randint(-100, -30)

    print("Node", i, "Signal Strength:", signal, "dBm")

    if signal > -60:
        print("Signal: Excellent")
    elif signal > -80:
        print("Signal: Good")
    else:
        print("Signal: Weak")
