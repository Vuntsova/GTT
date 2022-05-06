# is_male = True
# is_tall = True
#
# if is_male is False or is_tall:
#     print("io")
# else:
#     print("l;")
#
# if is_male is False and is_tall:
#     print("io")
# else:
#     print("l;")
#
# if is_male is False or is_tall is False:
#     print("io")
#
# elif is_male is False or is_tall:
#     print("pooopoopoprpooproproepopsdfpsfsdfsdf")
# else:
#     print("l;")
number1 = float(input("What is your number 1: "))
op = input("What is your operator: ")
number2 = float(input("What is your number 2: "))


if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "*":
    print(number1 * number2)
elif op == "/":
    print(number1 / number2)
else:
    print("Invalid Operator")
