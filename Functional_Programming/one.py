def f(x):
    return x + 2


def g(h, x):
    return h(x) * 2


print(g(f, 10))


def addx(x):
    def _(y):
        return x + y

    return _


addx2 = addx(2)
addx3 = addx(3)
print(addx2(2), addx3(3))
