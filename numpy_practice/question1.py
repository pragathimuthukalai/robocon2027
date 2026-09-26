import numpy as np

speeds = []
above20 =[]
for i in range(10):
    speed = float(input(f"Enter robot speed for time step {i + 1}: "))
    speeds.append(speed)

speed = np.array(speeds, dtype=float)

avg = np.mean(speed)
for i in range(len(speed)):
    if speed[i] < 10 or speed[i] > 100:
        print(f"Invalid speed : {speed[i]}")
for i in range(len(speed)):
    if speed[i] >20:
        print(f"Speed above 20: {speed[i]}")

for i in range(len(speed)):
    if speed[i] > 20:
        above20.append(speed[i])
count20 = np.count_nonzero(speed > 20)

speed += 5

speed[-5:] = 20

     
print("Speeds greater than 20 :", above20)
print(f"The robot above 20: {count20} ")
print("Speeds after adding 5 ", speed)
print(f"Average speed: {avg} ")
print("Final array:", speed)

