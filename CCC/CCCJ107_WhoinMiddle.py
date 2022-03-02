"""

In the story Goldilocks and the Three Bears, each bear had a bowl of oatmeal to eat while sitting at his/her favourite
chair. What the story didn't tell us is that Goldilocks moved the bowls around on the table, so the bowls were not at
the right seats anymore. The bowls can be sorted by weight with the lightest bowl being the Baby Bear's bowl, the medium
bowl being the Mama Bear's bowl and the heaviest bowl being the Papa Bear's bowl.

Write a program that reads in three weights and prints out the weight of Mama Bear's bowl. You may assume all weights
are positive integers less than 100.

Sample Input

10
5
8
Sample Output

8

"""

a = int(input())
b = int(input())
c = int(input())

if a > b > c or c > b > a:
    print(b)
elif a > c > b or b > c > a:
    print(c)
elif b > a > c or c > a > b:
    print(a)

