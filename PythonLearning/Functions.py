"""
Functions
#block of code - which can be exceuted
They can return something
they can't return something

they have parameters
they don't have parameters

Define --> and further call the function


def say_hello(): No return type, No parameter/Argument

    print(hello)

def say_hello(name):

    print ("hello" , name)

say_hello("shrenik")


def say_hello_default(name="shrenik")

    print ("hello",name)

say_hello_default()
"""
"""

def print_arg (*args):
    for i in args:
        print(i,end= " ")
print_arg(1,2,3)
"""

"""

r = max(1,2,3,5,4,6)
print("max=",r)
"""


"""
def make_pizza(*top,base):
    print(top,base)
    for i in top:
        print("list of all topping is:", i)

make_pizza("tomato","chilli flakes","onion", base="thin crust")
"""
def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print("list of all topping is:", topping)
    return toppings

shrenik_t=  make_pizza("tomato", "onion")
print(shrenik_t)




