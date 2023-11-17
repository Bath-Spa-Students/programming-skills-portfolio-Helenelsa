#Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 

#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
sandwich_orders = ['bacon', 'sausage', 'vegetable', 'cheese']
finished_sandwiches = []
while sandwich_orders:
    now_preparing = sandwich_orders.pop(0)
    print(f"I am making your {now_preparing} sandwich.")
    finished_sandwiches.append(now_preparing)

print('\n')
for sandwich in finished_sandwiches:
    print("I made your "+ sandwich, "sandwich")