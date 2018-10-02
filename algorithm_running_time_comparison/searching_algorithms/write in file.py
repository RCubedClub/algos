import random

f = open("decreasing.txt", "w")

for i in range(1000000):
    f.write(str(1000000-i))
    f.write(" ")

f.close()
print("Written")
