#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 

#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['chicken','pastrami', 'egg','pastrami' 'sausage', 'beef','pastrami']
finished_sandwiches = []

print("Leela has ran out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print("I am making your " + preparing_sandwich + " sandwich.")
    finished_sandwiches.append(preparing_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print("I made your "+ sandwich, "sandwich")