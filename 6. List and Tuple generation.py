'''     Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')    '''

values = input('Enter numbers seperated by commas: \n') # This line takes input numbers seperated by commas
list_ = values.split(',')                               # This line uses split method to seperate digits using coommas and stores it in a list variable
tuple_ = tuple(list_)                                   # This line stores list into a tuple

print('List: ', list_)
print('Tuple: ', tuple_)