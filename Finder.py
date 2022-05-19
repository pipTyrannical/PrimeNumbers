import time

primes = [2]
num = 3

preformance = True if input("Enable preformance mode? Y/N: ") == "y" else False
amountofprimes = int(input("Amount of primes you want to find: "))


if not preformance:
    q = time.perf_counter()
    while len(primes) < amountofprimes:
        print("Found: ", len(primes), "primes")
        for i in primes:
            if not num / i % 1:
                break

        else:
            primes.append(num)
        num += 2

else:
    q = time.perf_counter()
    print('Preformance mode on. This wont show any messages.')
    while len(primes) < amountofprimes:
        for i in primes:
            if not num / i % 1:
                break

        else:
            primes.append(num)
        num += 2


print(primes)
print(f"Finished in: ", time.perf_counter() - q)
