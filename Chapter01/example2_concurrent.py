# ch1/example2_sequential.py

import concurrent.futures
from timeit import default_timer as timer


# concurrent
def f(x):
    return x * x - x + 1


def concurrent_f():
    global result
    result = f(result)


if __name__ == '__main__':
    # ITERATIONS = 21 # concurrent gives variable results
    ITERATIONS = 20
    result = 3
    start = timer()

    with concurrent.futures.ThreadPoolExecutor(max_workers=ITERATIONS) as executor:
        futures = [executor.submit(concurrent_f) for i in range(ITERATIONS)]

        _ = concurrent.futures.as_completed(futures)

    print('Result is very large. Only printing the last 5 digits:', result % 100000)
    print('Result missing iterations: fˆ(N+1)', f(result) % 100000)
    print('Result missing iterations: fˆ(N+2)', f(f(result)) % 100000)
    print('Concurrent took: %.2f seconds.' % (timer() - start))
