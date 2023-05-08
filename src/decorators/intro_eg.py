##############################################
##### Functions are first class citizens #####
def compose(f, g, x):
    return f(g(x))

compose(print, len, "Hello, world!")
##############################################


###################################
##### Functions can be nested #####
import random

def random_power():
    def f(x):
        return x*x
    def g(x):
        return x*x*x
    def h(x):
        return x*x*x*x
    functions = [f, g, h]
    return random.choice(functions)

# for i in range(10):
#     p = random_power()
#     print(p(3))
###################################