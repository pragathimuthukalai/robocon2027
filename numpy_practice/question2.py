import numpy as np
reading = []
result=[]
invalid=[]
for i in range(10):
    r = int(input(f"Enter robot speed for time step {i + 1}: "))
    reading.append(r)
r = np.array(reading)
for i in range(len(r)):
    if r[i] < 10 or r[i] > 100:
        invalid.append(r[i])
    else:
        result.append(r[i])
# for i in range(10):
#     r = int(input(f"Enter robot speed for time step {i + 1}: "))
#     reading.append(r)
# r = np.array(reading)
# for i in range(len(r)):
#     if r[i] < 10 or r[i] > 100:
#         invalid.append(r[i])
#     else:
#         result.append(r[i])
# for i in range(10):
#     r = int(input(f"Enter robot speed for time step {i + 1}: "))
#     reading.append(r)
# r = np.array(reading)
# for i in range(len(reading)):
#     if reading[i] < 10 or reading[i] > 100:
#         invalid.append(reading[i])
#     else:
#         result.append(reading[i])
# print("Invalid speeds:", invalid)

print("Valid speeds:", result)