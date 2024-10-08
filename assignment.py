#question_one.py
# r is (4/3)* pie* r**2
#What is the volume of the sphere with radius 5.
# r= int(input("Enter the radius of the sphere: "))
# pie= int(input("Enter the value of pie: "))
# volume=((4/3)* pie* r**3)
# print(f"volume of the sphere: {volume}")

#Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

#Question_two.py
#area of a triangle (1/2* base* height).
#Base and height should be entered using the keyboard.

# base=int(input("Enter the base of a triangle: "))
# height=int(input("Enter the height of the triangle: "))
# area=(1/2* base* height)
# print(f"Area of a triangle: {area} ")
#Question_three.py
#WITI has tasked you to automate a simple grading system.
#As a python student, write a program used to display the grades that;
#the students will be receiving based on the mark scored in a subject.
#The grades are:
#90%-100% Grade is A
#80%-89% Grade is B
#70%-79% Grade is C
#60%-69% Grade is D
#50%-59% Grade is E
#<50% Fail
# def calculate_grades():
#     print("\n...Grade calculations...")
#     mark=int(input("Enter mark scored:\t"))
#     if mark>=90 and mark<=100:
#         print("Grade is A")
        
#     elif mark>=80 and mark<=89:
#         print("Grade is B")
        
#     elif mark>=70 and mark<=79:
#          print("Grade is C")
         
#     elif mark>=60 and mark<=69:
#         print("Grade is D")
        
#     elif mark>=50 and mark<=59:
#         print("Grade is E")
#     else:
#         print("Fail")
# #call the function
# calculate_grades()

#Question_four.py
#Sacco to help students save their money.
#Design a platform that will do the following.
#Welcome to,WITI Academy Sacco.
# 1. Deposit Money
# 2.Withdraw Money
# 3.Check Balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000
#If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#If the student selects 3, the account should be displayed.


def sacco_transactions():

    account_balance=0
    run=1
    while run==1:
        print("\nwelcome to, WITU Academy Sacco.")

        #menu
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')

        student_choice= int(input("Enter your selection(1,2,or 3):"))
        #performing the transactions basing on the student selection
    if student_choice == 1:
            print('\n...Processing a deposit transaction...')
            deposit_amount = int(input("Enter amount to be deposited: "))

            #check if deposit amount is less than 1000
    if deposit_amount < 1000:

                print('\nMinimum deposit is 1000')
    else:
                account_balance +=deposit_amount

                print(f"Dear student, you deposited {deposit_amount:,} and your new account balance is {account_balance:,}")


    if student_choice == 2:
        print('\n...Processing a withdraw transaction...')
        withdraw_amount = int(input("Enter amount to be withdrawn: "))


    if account_balance == 0:
        print("Your balance is 0")
    elif withdraw_amount < 500:
        print("Minimum withdraw amount is 500")

    elif withdraw_amount > account_balance:
        print(f" withdraw failed, insufficient funds")
    else:
        account_balance  -= withdraw_amount
        print(f"Dear student, you withdrawn {withdraw_amount:,} and your new account balance is {account_balance:,}")





    if student_choice == 3:
        print(f"Your new account balance is {account_balance:,}")

    else:  
        print("You entered a wrong choice! Please select 1, 2, or 3\n")



        run = int(input("Enter 1 to continue or any number to exit: "))
    if run!=1:
        print("Thanks for using our Sacco")

     

sacco_transactions()




    
 