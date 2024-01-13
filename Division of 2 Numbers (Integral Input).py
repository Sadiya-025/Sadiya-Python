A=input('Enter the First Number:\n')
B=input('Enter the Second Number:\n')
try:
    quotient=int(A)/int(B)
except ValueError:
    print('Invalid Datatype')
else:
    print('The value of A/B is',quotient)