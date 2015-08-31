__author__ = 'luchenhua'

EtoF = {'bread': 'du pain', 'wine': 'du vin', 'eats': 'mange', 'drinks': 'bois', 'likes': 'aime', 1: 'un',
        '6.00': '6.00'}
print(EtoF)
print(EtoF.keys())
print(EtoF.keys)
del EtoF[1]
print(EtoF)


def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word


def translate(sentence):
    translation = ''
    word = ''
    for e in sentence:
        if e != ' ':
            word = word + e
        else:
            translation = translation + ' ' + translateWord(word, EtoF)
            word = ''
    return translation[1:] + ' ' + translateWord(word, EtoF)


print(translate('John eats bread'))
print(translate('Steve drinks wine'))
print(translate('John likes 6.00'))


def simpleExp(b, n):
    if n == 0:
        return 1
    else:
        return b * simpleExp(b, n - 1)


print(simpleExp(2, 10))


def tower(n, f, t, s):
    if n == 1:
        print('Move from ' + f + ' to ' + t)
    else:
        tower(n - 1, f, s, t)
        tower(1, f, t, s)
        tower(n - 1, s, t, f)


print(tower(5, 'a', 'b', 'c'))


def toChars(s):
    import string

    s = string.lower(s)
    ans = ''
    for c in s:
        if c in string.lowercase:
            ans = ans + c
    return ans


def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1: -1])


def isPalindraw(s):
    return isPal(toChars(s))


print(isPalindraw('Guttag'))


def isPalPrint(s, indent):
    if len(s) <= 1:
        print(indent + 'current: ' + s)
        return True
    else:
        print(indent + 'current: ' + s)
        return s[0] == s[-1] and isPalPrint(s[1: -1], (indent + '  '))


def isPalindrawPrint(s):
    return isPalPrint(toChars(s), '  ')


print(isPalindrawPrint('Guttag'))


def fib(x):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
