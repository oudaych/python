def plus(x, y):
    return x + y

def moin(x, y):
    return x - y

def fois(x, y):
    return x * y

def sur(x, y):
    if y == 0:
        return
    return x / y

def calculatrice():
    print("Select operation:")
    print("1. plus")
    print("2. moin")
    print("3. fois")
    print("4. sur")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            
            if choice == '1':
                print ("The result is:",plus(num1, num2))
            elif choice == '2':
                print("The result is:",moin(num1, num2))
            elif choice == '3':
                print("The result is: ",fois(num1, num2))
            elif choice == '4':
                print("The result is: ",sur(num1, num2))

calculatrice()
 
