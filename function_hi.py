users_name = input("what is your name: ")
users_age = input("what is your age: ")


def say_hi(name, age):
    # or
    print("HI, " + name + " you are " + str(age) + " years old.")


say_hi(users_name, users_age)


def pow_this(what, to_the_power_of_what):
    return pow(what, to_the_power_of_what)


result = pow_this(3, 2)
print(result)
