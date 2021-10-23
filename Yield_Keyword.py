
'''The <yield> keyword in Python can turn any function into a generator'''


def testgen(index):
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    yield weekdays[index]
    yield weekdays[index + 1]
    day = testgen(0)
    print(next(day), next(day))

# A Simple Python program to demonstrate working
# of yield
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)




