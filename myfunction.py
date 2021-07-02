def Getmax(): #Getmax number that user enter
    Numberlist = []
    Number = 0
    index = 0
    Output = 0
    while True:
        try:
            Number = int(input('Enter your number: ')) #Get number from user
            Numberlist.append(Number) 
            if Numberlist[index] > Output:
                Output = Numberlist[index]
            index +=1
        except KeyboardInterrupt: # ctrl + c to exist 
            break 
    return Output 

def randomnumlist(length): #random number in list
    import random 
    numberlist = []
    count = 0
    while count != length:
        randnum = random.randint(1,9) #randomnumber between 1-9
        numberlist.append(randnum) #put the randomnumber to the List
        count+=1
    return numberlist

def Fibo(Seq): #Output Fibo seq
    Fibonacci = [1,1]
    count = 0
    index = 0
    while count != Seq:
        Fibonacci.append(Fibonacci[index] + Fibonacci[index+1]) 
        index +=1
        count +=1
    return Fibonacci[Seq-1]

def findfibo(inp): #to find is number in fibo seq
    Fibonacci = [1,1]
    index = 0
    while Fibonacci[index+1] <= inp: #loop until number in index >= input
        Fibonacci.append(Fibonacci[index] + Fibonacci[index+1]) 
        index +=1
    try:
        Fibonacci.index(inp) #if that number is in Fibonacci(list)
        print("Your number is Fibo!")
    except: #if number is not in list the program will error and run except
        print("Your number is not Fibo!")

def Factorial(n): #Factorial
    if n==1 and n>=0:
        return 1
    else:
        return n*Factorial(n-1)
