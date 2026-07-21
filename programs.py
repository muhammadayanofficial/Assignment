name = input("Enter Your Name: ")
Email = input("Enter Your Email: ")
Password = input("Enter Your Password: ")
Contact = input("Enter Your Contact: ")

print("\nAccount Created Successfully!\n")



emaillogin = input("Enter your login email: ")
passlogin = input("Enter your login Password: ")

if Email == emaillogin and Password == passlogin:

    print("\nWelcome", name)

    

    print("MARKSHEET")

    eng = int(input("Enter Your English Marks: "))
    urdu = int(input("Enter Your Urdu Marks: "))
    math = int(input("Enter Your Mathematics Marks: "))
    cs = int(input("Enter Your Computer Science Marks: "))
    islam = int(input("Enter Your Islamiat Marks: "))
    sindhi = int(input("Enter Your Sindhi Marks: "))
    phy = int(input("Enter Your Physics Marks: "))
    chem = int(input("Enter Your Chemistry Marks: "))

    total = eng + urdu + math + cs + islam + sindhi + phy + chem

    print("Total Marks =", total)

    per = total / 800 * 100

    print("Percentage =", per)

    if per >= 80:
        print("Grade A1")
    elif per >= 70:
        print("Grade A")
    elif per >= 60:
        print("Grade B")
    elif per >= 50:
        print("Grade C")
    elif per >= 40:
        print("Grade D")
    else:
        print("Fail")

    

    print("EVEN ODD DETECTOR")

    num = int(input("Enter Your Number: "))

    if num % 2 == 0:
        print("The Number Is Even")
    else:
        print("The Number Is Odd")



    print("Leap year")

    year = int(input("Enter Your Year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")


    print("Positive and negative")

    num = int(input("Enter Your Number: "))

    if num < 0:
        print("Negative")
    elif num > 0:
        print("Positive")
    else:
        print("Zero")



    print("Calculator")

    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    percent = (num1 / num2) * 100
    average = (num1 + num2) / 2

    print("Addition =", add)
    print("Subtraction =", sub)
    print("Multiplication =", mul)
    print("Division =", div)
    print("Percentage =", percent)
    print("Average =", average)

else:
    print("\nIncorrect Email or Password!")