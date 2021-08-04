import os


def list_pip(n):
    my_patch = "sort.txt"
    if os.path.getsize(my_patch) > 0:
        list_1 = [n]
        in_file = open("sort.txt", 'r').readlines()
        for line in in_file:
            line.index(line)
            list_1.append(line)
        return(list_1[n])