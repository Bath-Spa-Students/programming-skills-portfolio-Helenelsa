
#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

#* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

#their meanings as values.

#* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
#each word-meaning pair in your output.
Glossary={'type':'a built-in function that is used to return the type of data stored in the objects or variables in the program.',
          'int':'a whole number, positive or negative, without decimals',
          'dictionary':'A collection of key-value pairs,',
          'string':'A series of characters',
          'input':'request user input'}

print(f'\n','type:', Glossary['type'])
print(f'\n','int :', Glossary['int'])
print(f'\n','dictionary :', Glossary['string'])
print(f'\n','string :', Glossary['dictionary'])
print(f'\n','input :', Glossary['input'])