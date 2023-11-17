#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
Glossary={'type':'a built-in function that is used to return the type of data stored in the objects or variables in the program.',
          'int':'a whole number, positive or negative, without decimals',
          'dictionary':'A collection of key-value pairs,',
          'string':'A series of characters',
          'input':'request user input',
          'key': 'The first item in a key-value pair in a dictionary',
          'value': 'An item associated with a key in a dictionary',
          'conditional test': 'A comparison between two values',
          'float': 'A numerical value with a decimal component',
          'boolean expression': 'An expression that evaluates to True or False',}
for word, definition in Glossary.items():
    print("\n" + word.title() + ": " +definition)