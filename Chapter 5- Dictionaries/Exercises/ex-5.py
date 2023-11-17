#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

#each pet
Pets = [{"kind": "Dog", "owner": "Leo"},
    {"kind": "Fish", "owner": "Sam"},
    {"kind": "Hamster", "owner": "William"},
    {"kind": "Cat", "owner": "Tom"}]

for pet in Pets:
    print(f"Pet Kind: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
print()