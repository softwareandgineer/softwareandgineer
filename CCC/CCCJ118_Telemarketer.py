"""

Here at the Concerned Citizens of Commerce (CCC), we have noted that telemarketers like to use seven-digit phone numbers
where the last four digits have three properties. Looking just at the last four digits, these properties are:

the first of these four digits is an 8 or 9;
the last digit is an 8 or 9;
the second and third digits are the same.
For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers.

Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. If the
number is not a telemarketer number, we should answer the phone, and otherwise, we should ignore it.

Input Specification
The input will be 4 lines where each line contains exactly one digit in the range from 0 to 9.

Output Specification
Output either ignore if the number matches the pattern for a telemarketer number; otherwise, output answer.

Sample Input 1

9
6
6
8
Sample Output 1

ignore
Explanation for Sample Output 1
The first digit is , the last digit is , and the second and third digit are both , so this is a telemarketer number.

Sample Input 2

5
6
6
8
Sample Output 2

answer

"""

o = int(input())
tw = int(input())
th = int(input())
f = int(input())

if (o == 8 or o == 9) and (tw == th) and (f == 8 or f == 9):
    print("ignore")
else:
    print("answer")
