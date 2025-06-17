#user_name=input('Enter your name:')
#print (f'user_name: {user_name}')

#x=input('x= ')
#print (type(x))
#print(f'x*3= {int(x)*3}')


#print ('x')

try:
    x=int(input('x= '))
    print (f'x= {x}')
    print (3/x)
except ValueError:
    print ('x must be a number')
except ZeroDivisionError:
    print ('x cannot be zero') 
except:
    print ('some error occurred')



т


