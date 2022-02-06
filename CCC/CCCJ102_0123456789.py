"""
Most digital devices show numbers using a seven segment display. The seven segments are arranged as shown:

Copy
 * * *
*     *
*     *
*     *
 * * *
*     *
*     *
*     *
 * * *
For this problem, each segment is represented by three asterisks in a line as shown above.

Any digit from 0 - 9 can be shown by illuminating the appropriate segments. For example, the digit 1 may be displayed using the two segments on the right side:

Copy
      *
      *
      *

      *
      *
      *
The digit 4 needs four segments to display it properly:

Copy
*     *
*     *
*     *
 * * *
      *
      *
      *
Write a program that will accept a single digit input from the user, and then display that digit using a seven segment display. You may assume that each segment is composed of three asterisks.

DMOJ-specific note: None of your lines should contain any trailing whitespace. The last line must end with a newline.

Sample Input
Copy
9
Sample Output
Copy
 * * *
*     *
*     *
*     *
 * * *
      *
      *
      *
 * * *

"""

"""
My mapping method, each section has its own number
  1 1 1
 2     3
 2     3
 2     3
  4 4 4
 5     6
 5     6
 5     6
  7 7 7
"""

array = [
    [0, 1, 0, 1, 0, 1, 0],
    [2, 0, 0, 0, 0, 0, 3],
    [2, 0, 0, 0, 0, 0, 3],
    [2, 0, 0, 0, 0, 0, 3],
    [0, 4, 0, 4, 0, 4, 0],
    [5, 0, 0, 0, 0, 0, 6],
    [5, 0, 0, 0, 0, 0, 6],
    [5, 0, 0, 0, 0, 0, 6],
    [0, 7, 0, 7, 0, 7, 0],
]

"""
Below shows the information on which numbers uses which sections of the digital array
"""
digital_segments = [
    [1, 2, 3, 5, 6, 7], #0
    [3, 6], #1
    [1, 3, 4, 5, 7], #2
    [1, 3, 4, 6, 7], #3
    [2, 3, 4, 6], #4
    [1, 2, 4, 6, 7], #5
    [1, 2, 4, 5, 6, 7], #6
    [1, 3, 6], #7
    [1, 2, 3, 4, 5, 6, 7], #8
    [1, 2, 3, 4, 6, 7], #9
]

n = int(input())

for row in range(0, 9): #total rows
    str = ""
    for col in range(0, 7): #includes white spaces
        segment_num = array[row][col] #scans every spot in the array
        if segment_num in digital_segments[n]:
            str += "*"
        else:
            str += " "
    str = str.rstrip(" ") #gets rid of trailing whitespace
    print(str)
