result = ""
for i in range(1,10):
    if i ==1:
        result += "1st"
    elif i ==2:
        result += " 2nd"
    elif i ==3:
        result += " 3rd"
    else:
        result += " " + str(i) + "th"

print(result)