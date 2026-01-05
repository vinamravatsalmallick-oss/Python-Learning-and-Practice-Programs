# Day 7 of Python Programming

def greet(User_name):
    print("Hello", User_name)

def one_number_table_maker(A , B, C):
    for i in range(B, C + 1):
        print(f"{A} X {i} = {A*i}")
    print()
    print(f"Table of {A} is printed Above")

def multiple_number_table_maker(A, B, C, D):
    for m in range(A, B + 1):
        for i in range(C, D + 1):
            print(f"{m} X {i} = {m*i}", end="\t")
        print()   
    print()
    print(f"Table from {A} to {B} is written Above")
    
def rectangle_table_maker(A, B , C , D):
    for m in range(A, B + 1):
        for i in range(C, D + 1):
                print(f"{m*i}", end="\t")
        print()   
    print()
    print("Table is written Above")
    
def rectangle_number_pattern_maker(A,B):
    for m in range(1, A + 1):
        for i in range(1, B + 1):
            print(f"{i}", end="\t")
        print()   
    print()
    print("Pattern is Ready")
    
def rectangle_any_character_pattern_maker(A, B, C):
    for m in range(1, A + 1):
        for i in range(1, B + 1):
            print(C, end=" ")
        print()   
    print()
    print("Pattern is Ready")

def increasing_triangle_table_maker(A):
    for m in range(1, A + 1):
        for i in range(1, m + 1):
                print(f"{m*i}", end="\t")
        print()   
    print()
    print("Triangle Table is written Above")
    
def decreasing_table_triangle_maker(A):
    for m in range(A, 0 , -1):
        for i in range(1, m + 1 ):
                print(f"{m*i}", end="\t")
        print()   
    print()
    print("Triangle Table is constructed Above")

def increasing_number_triangle_maker(A,B):
    for m in range(A, B + 1):
        for i in range(A, m + 1):
                print(i, end="\t")
        print()   
    print()
    print(f"Triangle Pattern from {A} to {B} is generated above")

def decreasing_number_triangle_maker(A,B):
    if A > B:
        for m in range(A + 1, B, -1):
            for i in range(B, m ):
                    print(i, end=" ")
            print()   
        print()
        print(f"Triangle Pattern from {A} to {B} is generated above")
    elif A < B:
        for m in range(B + 1, A, -1):
            for i in range(A, m ):
                    print(i, end=" ")
            print()   
        print()
        print(f"Triangle Pattern from {A} to {B} is generated above")
      
def increasing_any_character_triangle_maker(B,C):
    for m in range(1, B + 1):
        for i in range(1, m + 1):
                print(C, end="\t")
        print()   
    print()
    print("Triangle Table is written Above")
    
def decreasing_any_character_triangle_maker(A,C):
    for m in range(A + 1, 0 , -1):
        for i in range(1, m ):
                print(C, end="\t")
        print()   
    print("Pattern is Ready")
    
def table_pyramid_maker(A):
    for m in range(1, A + 1):
        for i in range(1, m + 1):
                print(f"{m*i}", end="\t")
        print()
    for m in range(A - 1, 0 , -1):
        for i in range(1, m + 1 ):
                print(f"{m*i}", end="\t")
        print()   

    print()
    print("Pyramid Table is constructed Above")
   
def number_pyramid_maker(A):
    for m in range(1 ,A + 1):
        for i in range(1, m + 1):
                print(i, end=" ")
        print()   
    for m in range(A  , 0 , -1):
        for i in range(1, m ):
                print(i, end=" ")
        print()   
    print()
    print("Pyramid Number Pattern is constructed Above")
    
def any_character_pyramid_maker(A,B):
    for m in range(1 ,A + 1):
        for i in range(1, m + 1):
                print(B, end=" ")
        print()   
    for m in range(A - 1, 0 , -1):
        for i in range(1, m + 1 ):
                print(B, end=" ")
        print()   
    print()
    print("Pyramid Pattern is constructed Above")

def symmetric_table_maker(A):
    for m in range(A, 0 , -1):
        for i in range(1, m + 1 ):
                print(f"{m*i}", end=" ")
        print()
    for m in range(2, A + 1):
        for i in range(1, m + 1):
                print(f"{m*i}", end=" ")
        print()   
    print()
    print("Symmetric Table Pattern is Constructed Above")
    
def symmetric_number_maker(B):
    for m in range(B + 1, 1 , -1):
        for i in range(1, m ):
                print(i, end=" ")
        print()   
    for m in range(2 ,B + 1):
        for i in range(1, m + 1):
                print(i, end=" ")
        print()   
    print()
    print("Symmetric Number Pattern is constructed Above")
    
    
def symmetric_any_character_pattern_maker(B,C):
    for m in range(B + 1, 1 , -1):
        for i in range(1, m ):
                print(C, end=" ")
        print()   
    for m in range(2 ,B + 1):
        for i in range(1, m + 1):
                print(C, end=" ")
        print()   
    print()
    print("Symmetric Pattern is Constructed Above")
    
User_name = input("Enter Your Name:")
print()
greet(User_name)

print("Welcome to the Program")
print("This Program Generates Tables and Patterns")
print()
print("1.Tables")
print("2.Patterns")
print()
A = int(input("Enter Choice:"))

if A == 1:
    print()
    print("You Choose Table. Options are listed below:")
    print("1. Table of one number")
    print("2. Table of Multiple Number")
    print()
    A = int(input("Enter Choice (1/2):"))
    
    if A == 1:
        print()
        print("You Choose Table of One Number")
        print()
        A = int(input("Which number table do you want:"))
        B = int(input("Enter starting multiplier:"))
        C = int(input("Enter ending multiplier:"))
        print()
        one_number_table_maker(A, B, C)
    elif A == 2:
        print()
        print("You Choose Table of Multiple Number")
        print()
        A = int(input("Which number table do you want to start from:"))
        B = int(input("Which number table do you want to end from:"))

        C = int(input("Enter starting multiplier:"))
        D = int(input("Enter ending multiplier:"))
        print()
        multiple_number_table_maker(A, B, C, D)
elif A == 2:
    print()
    print("You Choose Patterns. Options are listed Below")
    print()
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Pyramid")
    print("4. Symmetric")
    print()
    A = int(input("Enter Choice(1/2/3/4):"))
    if A == 1:
        print()
        print("You Choose Rectangle. Options are listed below:")
        print()
        print("1. Table")
        print("2. Number")
        print("3. Any Character")
        print()
        A = int(input("Enter Choice(1/2/3):"))
        if A == 1:
            print()
            print("You Choose Table.")
            print()
            A = int(input("Which number table do you want to start from:"))
            B = int(input("Which number table do you want to end from:"))

            C = int(input("Enter starting multiplier:"))
            D = int(input("Enter ending multiplier:"))
            print()
            rectangle_table_maker(A, B, C, D)
        elif A == 2:
            print()
            print("You Choose Number Rectangle.")
            A = int(input("Choose Rows:"))
            B = int(input("Choose Columns:"))
            print()
            rectangle_number_pattern_maker(A, B)
        elif A == 3:
            print()
            print("You Choose Any Character")
            print()
            A = int(input("Choose Rows:"))
            B = int(input("Choose Columns:"))
            C = input("Enter Any Character/Number/Word/Sentence:")
            if C == int:
                int(C)
            rectangle_any_character_pattern_maker(A, B, C)
    elif A == 2:
        print()
        print("You Choose Triangle. Options are listed below:")
        print()
        print("1. Table")
        print("2. Number")
        print("3. Any Character")
        print()
        A = int(input("Enter Choice (1/2/3):"))
        if A == 1:
            print()
            print("You Choose Table. Options are listed below:")
            print()
            print("1. Increasing")
            print("2. Decreasing")
            print()
            A = int(input("Enter Choice (1/2):"))
            if A == 1:
                print()
                print("You Choose Increasing")
                print()
                A = int(input("Which number table do you want to end from:"))

                print()
                increasing_triangle_table_maker(A)
            elif A == 2:
                print()
                print("You Choose Decreasing")
                print()
                A = int(input("Which number table do you want to start from:"))
                
                print()
                decreasing_table_triangle_maker(A)
        elif A == 2:
            print()
            print("You Choose Number. Options are listed below:")
            print()
            print("1. Increasing")
            print("2. Decreasing")
            print()
            A = int(input("Enter Choice (1/2):"))
            if A == 1:
                print()
                print("You Choose Increasing")
                print()
                A = int(input("Enter Starting Number:"))
                B = int(input("Enter Ending Number:"))
                print()
                increasing_number_triangle_maker(A, B)
            elif A == 2:
                print()
                print("You Choose Decreasing")
                print()
                A = int(input("Enter Starting Number:"))
                B = int(input("Enter Ending Number:"))

                print()
                decreasing_number_triangle_maker(A, B)
        elif A == 3:
            print()
            print("You Choose Any Character. Options are listed below:")
            print()
            print("1. Increasing")
            print("2. Decreasing")
            print()
            A = int(input("Enter Choice (1/2):"))
            if A == 1:
                print()
                print("You choose Increasing")
                print()
                B = int(input("Enter Height Number:"))
                C = input("Enter Any Character/Number/Word/Sentence:")
                if C == int:
                    int(C)

                print()
                increasing_any_character_triangle_maker(B, C)
            elif A == 2:
                print()
                print("You Choose Decreasing")
                print()
                A = int(input("Enter First Star No:"))
                C = input("Enter Any Character/Number/Word/Sentence:")
                if C == int:
                    int(C)

                print()
                decreasing_any_character_triangle_maker(A, C)
    elif A == 3:
        print()
        print("You Choose Pyramid. Options are listed Below")
        print()
        print("1. Table")
        print("2. Number")
        print("3. Any Character")
        print()
        A = int(input("Enter Choice (1/2/3):"))
        if A == 1:
            print()
            print("You Choose Table")
            print()
            A = int(input("Enter Height Of Pyramid:"))

            print()
            table_pyramid_maker(A)
        elif A == 2:
            print()
            print("You Choose Number")
            print()
            A = int(input("Enter Height Of Pyramid:"))

            print()
            number_pyramid_maker(A)
        elif A == 3:
            print()
            print("You Choose Any Character")
            print()
            A = int(input("Enter Height of Pyramid:"))
            B = input("Enter Any Character/Number/Word/Sentence:")
            if B == int:
                int(B)

            print()
            any_character_pyramid_maker(A, B)

    elif A == 4:
        print()
        print("You Choose Symmetric. Options are listed below:")
        print()
        print("1. Table")
        print("2. Number")
        print("3. Any Character")
        print()
        A = int(input("Enter Choice (1/2/3):"))
        if A == 1:
            print()
            print("You Choose Table")
            print()
            A = int(input("Enter Starting No:"))
            print()
            symmetric_table_maker(A)
        elif A == 2:
            print()
            print("You choose Number")
            print()
            B = int(input("Enter Starting No:"))

            print()
            symmetric_number_maker(B)
        elif A == 3:
            print()
            print("You Choose Any Character")
            print()
            B = int(input("Enter Starting No:"))
            C = input("Enter Any letter/Word/Special Character/Star/Number/etc:")
            if C == int:
                int(C)
                
            print()
            symmetric_any_character_pattern_maker(B, C)
else:
    print("Invalid Choice")
print()
print("Developed By Vatsal")
print("Thanks For Using The Program")
print("Have a Good Day!")
             
        
    
    
    

