#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

#•	 If the alien is green, print a message that the player earned 5 points.

#	 If the alien is yellow, print a message that the player earned 10 points.

#•	 If the alien is red, print a message that the player earned 15 points.

#•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.
alien_color='Red'
if alien_color=='Yellow':
    print('Congratulations!, You just earned 5 points')
elif alien_color=='Yellow':
    print('Congratulations!, You just earned 15 points')
else:
    print('Congratulations!, You just earned 10 points ')

alien_color='Green'
if alien_color=='Red':
    print('Congratulations!, You just earned 10 points')

elif alien_color=='Yellow':
    print('Congratulations!, You just earned 15 points')
else:
    print('Congratulations!, You just earned 5 points ')

alien_color='Yellow'
if alien_color=='Green':
    print('Congratulations!, You just earned 5 points')
elif alien_color=='Yellow':
    print('Congratulations!, You just earned 5 points')
else:
    print('Congratulations!, You just earned 15 points ')