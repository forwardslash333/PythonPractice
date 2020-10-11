'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
Sample value of n is 5
Expected Result : 615
'''
n = input ('Enter an integer\n')
n1 = int('%s' % n)                                  # single digit integer
n2 = int('%s%s' % (n,n))                         # second digit number
n3 = int('%s%s%s' % (n,n,n))               # Three digit number

print(n1+n2+n3)