
# Implement clean_username(value). accept input from user The function should remove leading and trailing spaces, 
# convert the text to lowercase, and replace every space with an underscore. Return the cleaned username.

# solution 1:
def another(value):
    
    val1 = value.strip()
    val2 = val1.lower()
    result = val2.replace(" ", "/") 
    return result
print(another(input("enter your full name and age :")))





# solution 2:
def clean_username(value):
    step1 = value.strip().lower().replace(" ", "_")
    return step1
print(clean_username("emmanuel is my guy @ learn2earn"))