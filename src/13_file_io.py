"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

with open('foo.txt') as f:
    read_data = f.read()
f.closed
print(read_data)

# Had to move foo.txt up a level to make this work?


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# new_file = open('bar.txt', 'r+')
# new_file.write('Testing this \n Second line \n Third line')
# new_file.close()

b = open('bar.txt', 'w+')
b.write("Learning CS\n")
b.write("Learning Python\n")
b.write("More text\n")
b.closed

with open('bar.txt') as b:
    read_data = b.read()
b.closed
print(read_data)
