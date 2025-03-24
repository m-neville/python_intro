# functions
def area(radius):
    result = 22 / 7 * radius ** 2
    return result


def sayHi(name):
    print(" Good Morning", name)


print(area(7))  # called
print(area(6.5))
print(area(89.345))
sayHi("Neville")
sayHi("Maulid")

a1 = area(66.67)
print(round(a1 , 2))
