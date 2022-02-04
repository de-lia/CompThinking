file = open("Pycharmsample.txt", "r")  # Open file for reading
lines = file.readlines()
lines

count = 0
for line in lines:
    count = count + 1
    print(count, ": ", line, sep=" ", end=" ")

