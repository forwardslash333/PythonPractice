'''
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java           '''         # @jacob

filename= input('Enter the filename\n')     # Stores filename in a variable
extension = filename.split(".")             # Splits the file name by '.' and stores it in a list

print('File Extension is ', extension[-1])  # prints the last item of list