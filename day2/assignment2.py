# Q1. Define a variable of all the labours and print the name of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
#     labour variable should be something like this 1st_labour, 2nd_labour and so on.

# Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
#     labour variable should be something like this c,1st_labour_wage, 2nd_labour_name,
#     2nd_labour_wage and so on.
#     You are bound to use string formatting


# Q3. I want to print this paragraph and its line number from which this paragraph is printing
#     """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
#     we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
#     help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
#     we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
#             I have to print this paragraph as it is given here."""

#     Condition:- 
#     You can't use triple quote.
#     Triple quote at starting is also a part of paragraph.

# Q4. When do we get NameError?

# Q5. Python is a high level language. What does that mean by high level?

# Q6. What is compiled and Inetrpreted language, list a few?

# Q7. Get all varibales address from RAM and you find if something is similar?

# Answer1

first_labour = "Mahesh"
Second_labour = "Mithilesh"
Third_labour = "Ramesh"
Fourth_labour = "Sumesh"

# print(f'''first_labour :{first_labour}
# Second_labour :{Second_labour}
# Third_labour :{Third_labour}
# Fourth_labour :{Fourth_labour}
# ''')


First_labour_wage = 500
Second_labour_wage = 400
third_labour_wage = 300
Fourth_labour_wage =300
 
# print(f'''first_labour :{first_labour,First_labour_wage}
# Second_labour :{Second_labour,Second_labour_wage}
# Third_labour :{Third_labour,third_labour_wage}
# Fourth_labour :{Fourth_labour,First_labour_wage}
# ''')
print(f"first_labour : {first_labour} - ₹{First_labour_wage}")
print(f"Second_labour : {Second_labour} - ₹{Second_labour_wage}")
print(f"Third_labour : {Third_labour} - ₹{third_labour_wage}")
print(f"Fourth_labour : {Fourth_labour} - ₹{Fourth_labour_wage}")

# Answer3

print('''""" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
help of 'Python programming'. We have total land is of \\100 ft * 100ft /, to colmplete the house 
we have total 6 labours with 'different skill set like "\\\\ building wall or building roof \\\\".
        I have to print this paragraph as it is given here."""''')
# Answer4

print('''  
We get NameError when:

Variable/function/class not defined before use.

Spelling mistake in name.

Scope ke bahar variable ko access karna.
''')

# Answer5
print(f"first_labour : {first_labour}- {id(first_labour)} - ₹{First_labour_wage}-{id(First_labour_wage)}")
print(f"Second_labour : {Second_labour} - {id(Second_labour)}-₹{Second_labour_wage}-{id(Second_labour_wage)}")
print(f"Third_labour : {Third_labour} -{id(Third_labour)} -₹{third_labour_wage}-{id(third_labour_wage)}")
print(f"Fourth_labour : {Fourth_labour}-{id(Fourth_labour)} - ₹{Fourth_labour_wage}-{id(Fourth_labour_wage)}")


