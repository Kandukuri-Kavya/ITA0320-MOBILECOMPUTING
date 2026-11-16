nodes = ["A", "B", "C", "D"]

connections = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D")
]

print("Ad Hoc Network")

for connection in connections:
    print(connection[0], "<---->", connection[1])

print("\nData Transmission")
print("A sends data to B")
print("B forwards data to C")
print("C forwards data to D")
print("Data delivered successfully")
