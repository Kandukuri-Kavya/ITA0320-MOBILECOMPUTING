sent = 100
received = 90
time = 10

throughput = received / time
packet_delivery = (received / sent) * 100
packet_loss = sent - received

print("Network Performance")
print("Packets Sent:", sent)
print("Packets Received:", received)
print("Throughput:", throughput, "packets/sec")
print("Packet Delivery Ratio:", packet_delivery, "%")
print("Packet Loss:", packet_loss)
