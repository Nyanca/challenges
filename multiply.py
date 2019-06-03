def multiply():

    # initiate variable n to take input of int
    n = int(input("Pick a number from 1 - 30: "))
    
    # use for loop to iterate up to & including the input value
    for i in range(1, n+1):
        if n >= 30: 
            print 'Sorry, integer value too high.'
            break
        else:
    	   print(n,'x',i,'=',n*i)

multiply()