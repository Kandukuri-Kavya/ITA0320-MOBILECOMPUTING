users = ["User 1", "User 2", "User 3"]
resources = 9

print("OFDMA Scheduling")

for i in range(resources):
    user = users[i % len(users)]
    print("Resource Block", i + 1, "assigned to", user)
