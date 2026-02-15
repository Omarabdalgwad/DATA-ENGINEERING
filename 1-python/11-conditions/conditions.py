is_hungry = False
wants_to_eat = False

if is_hungry or wants_to_eat:
    print("go eat")
else:
    print("do not eat")

##

is_hungry = False
wants_to_eat = True

if is_hungry or wants_to_eat:
    print("go eat")
else:
    print("do not eat")

##

is_hungry = True
wants_to_eat = True

if is_hungry and wants_to_eat:
    print("go eat")
else:
    print("do not eat")

###

is_hungry = False
wants_to_eat = False

if is_hungry and wants_to_eat:
    print("go eat")
else:
    print("do not eat")

###

is_hungry = True
wants_to_eat = False

if is_hungry and wants_to_eat:
    print("eat")
elif is_hungry and not wants_to_eat:
    print("eat so you can survive")
else:
    print("do not eat")

##

is_hungry = False
wants_to_eat = True

if is_hungry and wants_to_eat:
    print("go eat")
elif is_hungry and not wants_to_eat:
    print("eat so you can survive")
elif not is_hungry and wants_to_eat:
    print("do not eat you are not hungry")
else:
    print("do not eat")
