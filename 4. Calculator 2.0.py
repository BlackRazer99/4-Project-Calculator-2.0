#calculator mit While schleifen und Functiones
def calculate (num1,num2,operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    return result

def calculateMore (num2,operator):
    if operator == "+":
        result = subResult + num2
    elif operator == "-":
        result = subResult - num2
    elif operator == "*":
        result = subResult * num2
    elif operator == "/":
        result = subResult / num2
    return result

loop = True
stopLoop = False
subResult = None

num1 = float(input("First number: "))
num2 = float(input("second number: "))
    
operator = input("Which Method would you like to use? ")
if operator == "+" or operator == "-" or operator == "*" or operator == "/" :    
    subResult = calculate(num1,num2,operator)
    print(subResult)
else:
    print("Operator doesn't exist")
    stopLoop = True
    
stop = input("Press yes to stop ")

if stop == "yes":
    loop = False
else:
    while loop != False and stopLoop == False :
        num2 = int(input("Input number: "))    
        operator = input("Which Method would you like to use? ")
        
        if operator == "+" or operator == "-" or operator == "*" or operator == "/" :
            subResult = calculateMore(num2,operator)
            print(subResult)
            stop = input("Press yes to stop ")
            if stop == "yes":
                loop = False
        else:
            print("operator doesn't exist")
        
if subResult != None:
    endResult = subResult
    print("Your result is ", endResult)
else:
    print("You don't have a Result")

input("prompt: ") 
