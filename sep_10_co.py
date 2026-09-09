# # we have to build our pace by doing more questions.
# # we are going to build a logic .
# # first , we have to input the user and sex of employee.

# # employee_name = input("ENTER THE NAME: ")
# # employee_sex = input("ENTER THE SEX:")

# # print(employee_name)
# # print(employee_sex)

# #step 2 : salary or bonus would be printed for women and men is 10% and 5%

# bonus_breganza = int(input("Enter the salary amount: "))
# bonus_1_breganza = int(input("Enter the salary amount: "))
# if bonus_breganza == 10 and employee_sex == "female":
#     print(bonus_breganza)
# elif bonus_1_breganza == 5 and employee_sex == "male":
#     print(bonus_1_breganza)

    #we keep remind that the logical expressions should be write in english and in literal for gender
    
    #kuch cheezein hai jo mujhe pehla invalid input aa kyon raha hai jabki variable ki conditioning sahi hai toh.
    #else statement hatane par mujhe kuch nahi mil raha hai
    
#step 3: display

#isme line 3 pe atak gaya hai aur isme true or false while loop se check karna hai abhi bhi yeh code incomplete hai 
employee_name = input("Enetr the name of an employee: ")
employee_sex = input("Enter the sex of employee: ")
bonus = float(input("Enter the mentioned bonus: "))
salary = float(input("enter the salary mentioned: "))
#don't forget the string and 
if employee_sex == "female" and bonus == 0.10 and salary == 10000:
    total_salary = salary + bonus
    print(total_salary)
    
elif employee_sex == "male" and bonus == 0.05 and salary == 10000:
    total_salary = salary + bonus
    print(total_salary)
else:
    print("invalid input")
    
# correct version of code:
    ch = input("Enetr the name: ")
    sal = int(input("enter the salary of the employee: "))
    if (ch == 'm'):
        bonus = 0.05*sal
    else:
        bonus = 0.10*sal
        
    amount_to_be_paid = sal + bonus
print("sal: ", sal)
print("bonus: ", bonus)
print("################")
print("THE TOtal salary: ", amount_to_be_paid)
    

    