"""
Two friends, Casper and Natalie went fishing. They caught a lot of fish. Casper pointed out that he had the longest fish
but Natalie said she had the heaviest fish. They agreed that they would determine the best fish as being the one whose
product of the weight and length was the largest.
Your job is to determine who caught the best fish.

Input Specification
The input begins with an integer C (≤ 10 000) which represents the total number of fish that Casper caught. Then each
of the records follows on its own line. Each record consists of two positive integers each less than 10 000: the weight
followed by the length of that particular fish. After these records, there is a number N (≤ 10 000) which represents the
total number of fish that Natalie caught.
On the next N lines, there is one record per line, as outlined above.

Output Specification
The output will be Casper if he has caught the best fish, or Natalie if she has caught the best fish, or Tie if they
caught equally good fish

Sample Input
3
10 3
3 11
4 4
4
10 2
29 1
16 2
6 6
Sample Output

Natalie

"""
import wc as wc

C = int(input())
mc = 0

for i in range(C):
    clst = input().split()
    w = int(clst[0]) * int(clst[1])
    if w > mc:
        mc = w

N = int(input())
nc = 0

for q in range(N):
    nlst = input().split()
    u = int(nlst[0]) * int(nlst[1])
    if u > nc:
        nc = u

if nc > mc:
    print("Natalie")
elif nc < mc:
    print("Casper")
else:
    print("Tie")



