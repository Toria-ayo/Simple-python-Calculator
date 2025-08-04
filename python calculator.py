#operation functions
def add(a,b): #addition
    return a+b
def sub(a,b): #subtraction
    return a-b
def mul(a,b): #multiplication
    return a*b
def div(a,b): #division
    return a/b
def sqr(a): #square
    return a**2
def sqr_root(a): #square root
    return a**0.5


#Head
print('CALCULATOR')
#available operations
print("""1: ADDITION
2: SUBTRACTION
3: MULTIPLICATION
4: DIVISION
5: SQUARE
6: SQUARE ROOT""")

while True:
    #operation chosen by user
    print('Which operation would you like to carry out, 1/2/3/4/5/6?')
    while True:
        try:
            choice=int(input())
            if 1<=choice<=6:
                break
            else:
                print('Please enter a number BETWEEN 1 and 6.')     
        except ValueError:
            print('Invalid input. Please enter a NUMBER between 1 and 6.')


    #Calculation operation begins
    msg='Enter a number to calculate; '
    if choice == 6:
        num=int(input(msg))
        result= sqr_root(num)
        print(f'The square root of {num} is; ,{result}')
    elif choice == 5:
        num=int(input(msg))
        result= sqr(num)
        print(f'The square of {num} is; {result}')
        
    else:
        #user input
        num1=int(input(msg))
        num2=int(input(msg))
        
        if choice == 1:
            result= add(num1, num2)
            print(f'The sum of {num1} and {num2} is; {result}')
            
        elif choice ==2:
            result= sub(num1, num2)
            print(f'The subtraction of {num2} from {num1} is; {result}')
        
        elif choice ==3:
            result= mul(num1, num2)
            print(f'The product of {num1} and {num2} is; {result}')
        
        elif choice ==4:
            if num2==0:
                result="Error: can't divide by 0"
            else:
                result= div(num1, num2)
            print(f'{num1} divided by {num2} is; {result}')


    #To repeat calculating based on user interest        
    again=input('\nDo you want to perform another operation, yes/no?\n')
    again=again.upper()
    if again !='YES':
        print('THANKS FOR USING THIS CALCULATOR')
        break

    
