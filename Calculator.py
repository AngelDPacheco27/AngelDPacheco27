#Rudimental Calculator using Python VS Code
#Coded by Angel Pacheco, Boston Univeristy, August 2024

#This Calculator Supports: Multiplication, Subtraction, Addition, Division, Exponentiation, Modulus, and Floor Division
#Only Acceptes Postive Whole Numbers From The User For Now

#Functions
        
#Checks If The Operation Will Be Dividing By 0
def check_zero(num_2):
    while num_2 == 0:
        print("Cannot Divide By 0 Enter A New Number")
        num_2 = input()
        print()
        num_2 = verify_num(num_2)

    return num_2

#Calculates Final Answer
def calculate_ans(oper, num_1, num_2):


    if oper == "A":
        final_ans = num_1 * num_2
        print("Your Answer is", final_ans)
            
    elif oper == "B":
        num_2 = check_zero(num_2)
        final_ans = num_1 / num_2
        print("Your Answer is", final_ans)
            
    elif oper == "C":
        final_ans = num_1 + num_2
        print("Your Answer is", final_ans)
            
    elif oper == "D":
        final_ans = num_1 - num_2
        print("Your Answer is", final_ans)
            
    elif oper == "E":
        final_ans = num_1 ** num_2
        print("Your Answer is", final_ans)
            
    elif oper == "F":
        num_2 = check_zero(num_2)
        final_ans = num_1 % num_2
        print("Your Answer is", final_ans)

    elif oper == "G":
        num_2 = check_zero(num_2)
        final_ans = num_1 // num_2
        print("Your Answer is", final_ans)

    print()
    return final_ans

#Checks if the Letter Entered for an Operations is Valid
def verify_oper(oper):
    while oper.upper() != "A" and oper.upper() != "B" and oper.upper() != "C" and oper.upper() != "D" \
        and oper.upper() != "E" and oper.upper() != "F" and oper.upper() != "G":
    
        print("Please Enter The Letter For Your Operation")
        print()
        oper = input()
        
    return oper.upper()

#Checks if the user input is an actual number
def verify_num(num):
    while num.isnumeric() == 0: 
        print("Please Enter A Positive Whole Number")
        num = input()
        print()
        
    num = float(num)
    return num

#Checking If User Entered A Valid Response
def verify_response(response):
    while response.lower() != "yes" and response.lower() != "no":
        print("Please Enter Yes or No")
        response = input()
        print()
    return response.lower()

#Introducing & Requesting Number of Operation
restart = True

while restart == True:
    print("Hello Welcome to your Calculator")
    print("A = Multiplication")
    print("B = Division")
    print("C = Additon")
    print("D = Subtraction")
    print("E = Exponentiation")
    print("F = Modulus")
    print("G = Floor Division")
    print()


    #Inputting Numbers and Operation

    print("Enter Your 1st Number")
    num_1 = input()
    print()
    num_1 = verify_num(num_1)
    

    print("Enter Letter of Desired Operation")
    oper = input()
    print()
    oper = verify_oper(oper)

    print("Enter Your 2nd Number")
    num_2 = input()
    print()
    num_2 = verify_num(num_2)

    #Calculating Answer Function


    final_ans = calculate_ans(oper, num_1, num_2)

    #Continuing Operation via While Loop

    print("Do You Wish To Do Another Operation On Your Number? Yes or No?")
    response_1 = input()
    print()
    response_1 = verify_response(response_1)


    #Performs Another Operation on Previous Answer
    while response_1 == "yes":

        print("Enter Desired Operation")
        oper = input()
        print()
        oper = verify_oper(oper)

        print("Enter new number")
        num_2 = input()
        print()
        num_2 = verify_num(num_2)
        
        final_ans = calculate_ans(oper, final_ans, num_2)
        
        print("Do You Wish To Do Another Operation On Your Number? Yes or No?")
        response_1 = input()
        print()
        response_1  = verify_response(response_1)

    #Asks whether the user want to start a new calculation and reset loop
    if response_1 == "no":
        print("Do You Want Start A New Calculation? Yes or No?")
        response_2 = input()
        print()
        response_2 = verify_response(response_2)

        match response_2:

            case "yes":
                restart = True
            
            case "no":
                restart = False

print("Thank You Have a Good Day!")
print()