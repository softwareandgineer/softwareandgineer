"""
Canada Cosmos Control has received a report of another incident. They believe that an alien has illegally entered our
space. A person who witnessed the appearance of the alien has come forward to describe the alien's appearance. It is your role within the CCC to determine which alien has arrived. There are only 3 alien species that we are aware of, described below:

TroyMartian, who has at least 3 antennae and at most 4 eyes;
VladSaturnian, who has at most 6 antennae and at least 2 eyes;
GraemeMercurian, who has at most 2 antennae and at most 3 eyes.
Input Specification
The first line will contain the number of antennae that the witness claimed to have seen on the alien.

The second line will contain the number of eyes seen on the alien.

Output Specification
The output will be the list of aliens who match the possible description given by the witness. If no aliens match the
description, there is no output.

Sample Input 1

4
5
Output for Sample Input 1

VladSaturnian
Sample Input 2

2
3
Output for Sample Input 2

VladSaturnian
GraemeMercurian
Sample Input 3

8
6
Output for Sample Input 3


"""

ant = int(input())
eyes = int(input())

if ant >= 3 and eyes <= 4:
    print("TroyMartian")
if ant <= 6 and eyes >= 2:
    print("VladSaturnian")
if ant <= 2 and eyes <= 3:
    print("GraemeMercurian")
    
