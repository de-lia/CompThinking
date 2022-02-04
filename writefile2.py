out_1 = open("out_1.txt", "w")
out_2 = open("out_2.txt", "w")
values_1 = ["one", "two", "three"]
values_2 = ["one\n", "two\n", "three\n"]
out_1.writelines(values_1)
out_2.writelines(values_2)

