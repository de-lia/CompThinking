file = open("info.txt")
count = 0
for line in file:
    count = count + 1
    print(count, ": ", line, sep=" ", end=" ")
    