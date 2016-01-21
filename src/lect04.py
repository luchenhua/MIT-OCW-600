__author__ = 'luchenhua'


def withinEpsilon(x, y, epsilon):
    return abs(x - y) <= epsilon


print(withinEpsilon(2, 3, 1))


def f(x):
    x += 1
    print('x = ', x)
    return x


x = 3
z = f(x)
print('z =', z)
print('x =', x)


def f1(x):
    def g():
        x = 'abc'
        print('x =', x)

    x += 1
    print('x =', x)
    g()
    return x


x = 3
z = f1(x)
print('z =', z)
print('x =', x)


def isEven(i):
    return i % 2 == 0


def findRoot(pwr, val, epsilon):
    assert type(pwr) == int and type(val) == float and type(epsilon) == float
    assert pwr > 0 and epsilon > 0
    if isEven(pwr) and val < 0:
        return None
    low = -abs(val)
    high = max(abs(val), 1.0)
    ans = (high + low) / 2.0
    while not withinEpsilon(ans ** pwr, val, epsilon):
        if ans ** pwr < val:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans


def testFindRoot():
    for x in (-1.0, 1.0, 3456.0):
        for pwr in (1, 2, 3):
            ans = findRoot(pwr, x, 0.001)
            if ans is None:
                print('The answer is imaginary')
            else:
                print(ans, 'to the power', pwr, 'is close to', x)


testFindRoot()

sumDigits = 0
for c in str(1984):
    sumDigits += int(c)
print(sumDigits)
