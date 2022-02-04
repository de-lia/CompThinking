file = open("info.txt", "r")
line_one = file.readline()
line_two = file.readline()
for line in file.readlines():
    print(line, end="")