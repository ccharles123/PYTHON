name = "Mariana"
lastName = "Hernandez López"
age = 10

print(name)
print(lastName)

fullName = name + " " +lastName
print(fullName)

#format

quote = "I am " + name + ", my last name is " + lastName + ", I am " + str(age) +  " years old"
print("v1", quote)

quote2 = "I am {}, my last name is {}, I am {} years old".format(name, lastName, age) 
print("v2", quote2)

quote3 = f"I am {name}, my last name is {lastName}, I am {age} years old"
print("v3", quote3)