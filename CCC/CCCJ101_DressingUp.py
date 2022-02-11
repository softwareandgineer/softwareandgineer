"""
It is important to keep our computers safe and clean. Some people feel that computers should be well-dressed, also. For
this question, you will write a program to print out a bow tie on the computer screen.

Your program should take as input the height  of the bow tie, where  is an odd positive integer greater than or equal to
5. A bow tie with  rows (and  columns) should then be printed using the pattern shown below in the sample output.

Input Specification
One line containing integer . You may assume that all input data will be valid.

Sample Input 1
5
Sample Output 1
*        *
***    ***
**********
***    ***
*        *
Sample Input 2
7
Sample Output 2
*            *
***        ***
*****    *****
**************
*****    *****
***        ***
*            *
"""

H = int(input())
stars = 1
steps = 2
for i in range(H):
    for j in range(1, 2*H+1):
        if j <= stars:
            print("*", end="")
        elif 2 * H + 1 - j <= stars:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
    stars += steps
    if stars == H:
        steps = -steps





