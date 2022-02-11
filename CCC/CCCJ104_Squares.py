"""
Gigi likes to play with squares. She has a collection of equal-sized square tiles. Gigi wants to arrange some or all of
her tiles on a table to form a solid square. What is the side length of the largest possible square that Gigi can build?

For example, when Gigi has 9 tiles she can use them all to build a square whose side length is 3. But when she has only
8 tiles, the largest square that she can build has side length 2.

Write a program that inputs the number of tiles and then prints out the maximum side length. You may assume that the
number of tiles is less than ten thousand.

Sample Input 1
9
Sample Output 1
The largest square has side length 3.

Sample Input 2
8
Sample Output 2
The largest square has side length 2.

Sample Input 3
7535
Sample Output 3
The largest square has side length 86.
"""

import math

n = int(input())
y = math.sqrt(n)
y = int(y)
print(f"The largest square has side length {y}.")
