from functools import reduce
import test


def str2num(s):
    # x = int(s)
    try:
        x = int(s)
    except Exception as e:
        # print("error:", e)
        x = float(s)
    return x


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
test.move(5, "A", "B", "C")
Bob = test.Student()
Bob.score = 100
print(Bob.score)