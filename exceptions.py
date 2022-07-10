#try
#except
#raise
#else
#finally
# x = int(input('enter first number: '))
# y = int(input('enter second number: '))
x = 10
y = 2
try:
    if y == 0:
        raise Exception('The denominator is 0')
    print(x / y)
except Exception as e:
    print(e)
else:
    print('This is else block.')
finally:
    print('finally is always executed.')
