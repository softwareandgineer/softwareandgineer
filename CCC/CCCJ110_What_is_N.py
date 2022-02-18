"""

Natalie is learning to count on her fingers. When her Daddy tells her a number n(1 <= n <= 10) , she asks "What is ,
Daddy?", by which she means "How many fingers should I hold up on each hand so that the total is n?"

To make matters simple, her Daddy gives her the correct finger representation according to the following rules:

the number may be represented on one or two hands;
if the number is represented on two hands, the larger number is given first.
For example, if Natalie asks "What is 4, Daddy?", her Dad may reply:

4 is 4.
4 is 3 and 1.
4 is 2 and 2.
Your job is to make sure that Natalie's Daddy gives the correct number of answers.

Input Specification
The input will be a single integer i such that 1 <= i <= 10.

Output Specification
The output is the number of ways of producing that number on two hands, subject to the rules outlined above.

Sample Input

4
Output for Sample Input

3

"""

n = int(input())
a = (n - 1)
b = (n - 2)
c = (n - 3)
d = (n - 4)
e = (n - 5)
i = 0

if n <= 5:
    i += 1
if 0 <= a <= 5:
    if a >= 1:
        i += 1
if 0 <= b <= 5:
    if b >= 2:
        i += 1
if 0 <= c <= 5:
    if c >= 3:
        i += 1
if 0 <= d <= 5:
    if d >= 4:
        i += 1
if 0 <= e <= 5:
    if e >= 5:
        i += 1

print(i)

