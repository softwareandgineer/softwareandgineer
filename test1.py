
for i in range(1, 10):
    line = ""
    for j in range(1,10):
        if i >= j:
            line += f"{i}*{j}={i*j} "

    print(line)
