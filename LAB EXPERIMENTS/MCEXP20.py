print("AD HOC NETWORK TROUBLESHOOTING")

signal = int(input("Enter signal strength: "))
battery = int(input("Enter battery percentage: "))
connected = input("Is network connected? (yes/no): ")

if signal < -80:
    print("Problem: Weak Signal")
    print("Solution: Move closer to the node")

elif battery < 20:
    print("Problem: Low Battery")
    print("Solution: Charge the device")

elif connected == "no":
    print("Problem: Connection Lost")
    print("Solution: Restart network")

else:
    print("Network is Working Properly")
