file = open("info2.txt", "r")
file.tell()
print(file.tell())

all = file.read()
file.tell()
print(file.tell())
print(len(all))