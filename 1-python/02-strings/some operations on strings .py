#  str with backslach
print("exam\nples") 
print("exam\"ples")
print("exam\ples")
print("exam\tples")

text = "examples"
print(text)
print("very simple " + text) #concatenation

# str with simple functions

name = "OmAr"
print(name.lower()) #convert capital letters into small letters
print(name.upper()) #convert small letters into capital letters
print(name.isupper()) #to check --> the output will be true or false
print(name.islower()) #to check --> the output will be true or false
print(name.lower().islower()) #use multiple functions one after another (واحده ورا واحده ) 
print(len(name))  #lenth of the string --> the output will be int
print(name[0])    #indexing a letter of the str --> start from 0 not 1
print(name.index("A")) #to find the index of a letter
print(name.replace("Om","Qm")) #replace substring by anthor