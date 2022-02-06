"""
Write a program to print out a calendar for a particular month given the day on which the first of the month occurs
together with the number of days in the month.

Your program should take as input an integer representing the day of the week on which the month begins
(1 for Sunday, 2 for Monday, …, 7 for Saturday), and an integer which is the number of days in the month (between 28 and
 31 inclusive). Your program should print the appropriate calendar for the month. You can assume that all input data
 will be valid.

Input:
3 30

Output:
Sun Mon Tue Wed Thr Fri Sat
          1   2   3   4   5
  6   7   8   9  10  11  12
 13  14  15  16  17  18  19
 20  21  22  23  24  25  26
 27  28  29  30

"""

day_of_week, days_in_month = input().split()
day_of_week = int(day_of_week)
days_in_month = int(days_in_month)

print("Sun Mon Tue Wed Thr Fri Sat")
count = 0
for i in range(2-day_of_week, days_in_month+1):
    if i < 1:
        print("   ", end="")
    else:
        print("{:>3}".format(i), end="")

    count += 1

    if count % 7 == 0 or i == days_in_month:
        print("")
    else:
        print(" ", end="")




