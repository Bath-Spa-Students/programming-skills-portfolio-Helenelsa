#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

#medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size=' Large',message='I love python'):
    summary =('\n''Creating a'+ size +'-sized shirt with the message:'+message)
    print(summary)

#default message
make_shirt()

#medium size 
make_shirt(size=" Medium")
make_shirt(size=" Small", message="Hello")