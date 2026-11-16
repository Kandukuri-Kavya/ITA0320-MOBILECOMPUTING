import numpy as np

user1 = np.array([1, 1, 1, 1])
user2 = np.array([1, -1, 1, -1])

data1 = 1
data2 = -1

combined = data1 * user1 + data2 * user2

print("Combined Signal:", combined)

print("User 1 Data:", np.dot(combined, user1) // 4)
print("User 2 Data:", np.dot(combined, user2) // 4)
