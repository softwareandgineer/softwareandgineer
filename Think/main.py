width = 19


def get_edge(width, i, j):
    hw = width//2
    if i < hw and j < hw:
        return min(i,j)

    elif i < hw and j >= hw:
        return min(i, width - j)

    elif i >= hw and j < hw:
        return min(width - i, j)

    else:
        return min(width - i, width - j)



for i in range(width + 1):
    line = ""
    for j in range(width + 1):
        n = get_edge(width, i, j)+1
        line += str(n) + "\t"
    print(line)
