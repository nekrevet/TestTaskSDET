from datetime import datetime


def get_fib():
    count_fib = int(str(datetime.today())[8:10]) + 1
    i = 0
    res = [1, 1]
    while len(res) < count_fib:
        res.append(sum(res[i:]))
        i += 1
    return res[-1]


class Amount:
    AMOUNT = get_fib()
