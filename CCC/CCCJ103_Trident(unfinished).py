"""
A trident is a fork with three tines (prongs). A simple picture of a trident can be made from asterisks and spaces:

*  *  *
*  *  *
*  *  *
*******
   *
   *
   *
   *
In this example, each tine is a vertical column of 3 asterisks. Each tine is separated by 2 spaces. The handle is a
vertical column of 4 asterisks below the middle tine.

Tridents of various shapes can be drawn by varying three parameters: , the height of the tines, , the spacing between
tines, and , the length of the handle. For the example above we have , , and .

You are to write an interactive program to print a trident. Your program should accept as input the parameters , , and ,
and print the appropriate trident. You can assume that , ,  are each at least 0 and not larger than 10.

Sample Input
4
3
2
Sample Output
*   *   *
*   *   *
*   *   *
*   *   *
*********
    *
    *

"""
h = 0
spc = 0
length = 0


