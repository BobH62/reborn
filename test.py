def move(nn, a, b, c):
    if nn == 1:
        print(a, "-->", c)
    else:
        move(nn - 1, a, c, b)
        move(1, a, b, c)
        move(nn - 1, b, a, c)


def _it_odd():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _it_odd()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


class Student(object):
    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must be between 0~100")
        self._score = value


def f(*args, **kwargs):
    pass


print("I love MM")

# Bob = Student()
# Bob.score = 100
# print(Bob.score)


# move(5, "A", "B", "C")
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
