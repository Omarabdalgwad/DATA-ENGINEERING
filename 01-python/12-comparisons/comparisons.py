"""
comparison operators:
==
!=
>
<
>=
<=

"""
#examples

def max_num(num1,num2,num3):
    if num1>= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
          return num2
    else:
         return num3
print(max_num(1,4,7))

# this is implemented in python as a built-in function --> max()

print(max(1,4,7))

##

def match_string(str1,str2):
    if str1 == str2:
         print("the strings do match")
    else:
         print("the strings don't match")
match_string("omar","omar")