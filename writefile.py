file_in = open("info.txt", "r")
file_out = open("info_lined.txt", "w")
count = 0
for line in file_in:
    count = count + 1
    file_out.write("{:2d}: {}".format(count, line))