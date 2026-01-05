# Day 4 of Python

a = int(input("Enter Your Present days in School:"))
e = int(input("Enter Total number of School days:"))
g = a / e * 100

if g >= 75:
    print(f"You got {g:.2f}% attendance")
    d = int(input("Enter Class:"))
    b = int(input("Enter Your Marks obtained:"))
    f = int(input("Enter Total Marks:"))
    c = b / f * 100 
    print(f"You obtained {c:.2f}% marks")
    if c >= 33:
        print(f"You are Promoted to {d + 1} class")
    else:
        print("Not Promoted")
    if c >= 90:
           print("Your Grade is A")
    elif c >= 80:
          print("Your Grade is B")
    elif c >= 70:
        print("Your Grade is C")
    elif c >= 60:
        print("Your Grade is D")
    elif c >= 50:
        print("Your Grade is E")
    elif c >= 33:
        print("Just Pass, Try Harder")
    else:
        print("Failed")
        
else:
    print(f"You got {g:.2f}% attendance")
    print("Attendence requirement is not matched")
    
 

    
