def get_grades(grades):
    if grades >= 75:
        print("First")
    elif grades >= 70 and grades < 75:
        print("Upper Second")
    elif grades >= 60 and grades < 70:
        print("Second")
    elif grades >= 50 and grades < 60:
        print("Third")
    elif grades >= 45 and grades < 50:
        print("F1 Supp")
    elif grades >= 40 and grades < 45:
        print("F2")
    elif grades < 40:
        print("F3")

print(get_grades(79))



