nodes = ["A", "B", "C", "D"]

print("DSDV Routing")
print("Routing table maintained continuously")

for node in nodes:
    print(node, "updates routing table")

print("\nAODV Routing")
print("Route requested only when needed")

print("A sends Route Request")
print("B forwards request")
print("C forwards request")
print("D sends Route Reply")
print("Route established successfully")
