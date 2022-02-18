"""

Many communities now have "radar" signs that tell drivers what their speed is, in the hope that they will slow down.

You will output a message for a "radar" sign. The message will display information to a driver based on his/her speed
according to the following table:

km/h over the limit	Fine
1 to 20	$100
21 to 30	$270
31 or above	$500
Input Specification
The user will be prompted to enter two integers. First, the user will be prompted to enter the speed limit. Second, the
user will be prompted to enter the recorded speed of the car.

Output Specification
If the driver is not speeding, the output should be: Congratulations, you are within the speed limit!

If the driver is speeding, the output should be: You are speeding and your fine is $F. where F is the amount of the fine
as described in the table above.

Sample Input 1

40
39
Sample Output 1

Congratulations, you are within the speed limit!
Sample Input 2

100
131
Sample Output 2

You are speeding and your fine is $500.
Sample Input 3

100
120
Sample Output 3

You are speeding and your fine is $100.

"""

limit = int(input())
speed = int(input())

F = int(speed - limit)

if F <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= F <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= F <= 30:
    print("You are speeding and your fine is $270.")
elif 31 <= F:
    print("You are speeding and your fine is $500.")

