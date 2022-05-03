import time

primes = [2]
num = 3


amountofprimes = int(input("Amount of primes you want to find: "))

q = time.perf_counter()
while len(primes) < amountofprimes:
    print("Found: ", len(primes), "primes")
    for i in primes:
        if not num / i % 1:
            break

    else:
        primes.append(num)
    num += 2

print(primes)
print(f"Finished in: ", time.perf_counter() - q)
