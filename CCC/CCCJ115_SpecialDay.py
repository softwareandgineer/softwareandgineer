"""

February 18 is a special date for the CCC this year.

Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that
date occurs before, after, or on February 18.

If the date occurs before February 18, output the word Before.
If the date occurs after February 18, output the word After.
If the date is February 18, output the word Special.
Input Specification
The input consists of two integers each on a separate line. These integers represent a date in .

The first line will contain the month, which will be an integer in the range from  (indicating January) to
(indicating December).

The second line will contain the day of the month, which will be an integer in the range from  to . You can assume that
the day of the month will be valid for the given month.

Output Specification
Exactly one of Before, After, or Special will be printed on one line.

Sample Input 1

1
7
Output for Sample Input 1

Before
Sample Input 2

8
31
Output for Sample Input 2

After
Sample Input 3

2
18
Output for Sample Input 3

Special

"""

month = int(input())
day = int(input())

if month < 2:
    print("Before")
elif month > 2:
    print("After")
elif month == 2 and day > 18:
    print("After")
elif month == 2 and day < 18:
    print("Before")
elif month == 2 and day == 18:
    print("Special")