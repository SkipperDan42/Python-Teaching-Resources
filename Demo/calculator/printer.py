import calulator as calc

def printCaluclations(x,y):
    print(f"x + y = {calc.add(x, y)}")
    print("x - y = {}".format(calc.subtract(x, y)))
    print("x * y = %d" % (calc.multiply(x, y)))
    print("x / y =", str(calc.divide(x, y)))