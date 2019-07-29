import math
from functools import lru_cache
from time import time


def print_execution_time(function):
    def timed(*args, **kw):
        time_start = time()
        return_value = function(*args, **kw)
        time_end = time()

        execution_time = time_end - time_start

        arguments = ", ".join(
            [str(arg) for arg in args] + ["{}={}".format(k, kw[k]) for k in kw]
        )

        print(
            "{} ms {}({})".format(
                str(execution_time * 1000), function.__name__, arguments
            )
        )
        return return_value

    return timed


@lru_cache(None)
def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@print_execution_time
def calculate_factorial(n: int) -> int:
    return factorial(n)


@print_execution_time
def stirlings(n: int) -> int:
    return math.floor(math.sqrt((2 * n + 1 / 3) * math.pi) * n ** n * math.e ** (-n))


if __name__ == "__main__":
    n = 140
    f = calculate_factorial(n)
    s = stirlings(n)
    print(f"n = {n}: diff {100*((f-s)/f)}% \nfactorial = {f} \nstirlings = {s} ")
    # for n in range(1, 20):
    #     f = factorial(n)
    #     s = stirlings(n)
    #     print(f"n = {n}: diff {100*((f-s)/f)}% \t factorial = {f} \t stirlings = {s} ")
