"""

Moe Bull has a cell phone and after a month of use is trying to decide which price plan is the best for his usage
pattern. He has two options, each plan has different costs for daytime minutes, evening minutes and weekend minutes.

Plan	Costs
daytime	evening	weekend
A	100 free minutes then 25 cents per minute	15 cents per minute	20 cents per minute
B	250 free minutes then 45 cents per minute	35 cents per minute	25 cents per minute
Write a program that will input the number of each type of minutes and output the cheapest plan for this usage pattern,
using the format shown below. The input will be in the order of daytime minutes, evening minutes and weekend minutes.
In the case that the two plans are the same price, output both plans.

Sample Input 1

251
10
60
Sample Output 1

Plan A costs 51.25
Plan B costs 18.95
Plan B is cheapest.
Sample Input 2

162
61
66
Sample Output 2

Plan A costs 37.85
Plan B costs 37.85
Plan A and B are the same price.

"""
day = int(input())
eve = int(input())
wkn = int(input())

if day >= 100:
    PlanA = ((day - 100) * 25 + eve * 15 + wkn * 20)/ 100
else:
    PlanA = (eve * 15 + wkn * 20) / 100

if day >= 250:
    PlanB = ((day - 250) * 45 + eve * 35 + wkn * 25) / 100
else:
    PlanB = (eve * 35 + wkn * 25) / 100

if PlanA > PlanB:
    print("Plan A costs " + str(PlanA))
    print("Plan B costs " + str(PlanB))
    print("Plan B is cheapest.")
elif PlanA < PlanB:
    print("Plan A costs " + str(PlanA))
    print("Plan B costs " + str(PlanB))
    print("Plan A is cheapest.")
else:
    print("Plan A costs " + str(PlanA))
    print("Plan B costs " + str(PlanB))
    print("Plan A and B are the same price.")





