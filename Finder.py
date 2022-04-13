import time

primes = [2]
num = 3

q = time.time()
amountofprimes = int(input("Amount of primes you want to find: "))

while len(primes) < amountofprimes:
    print("Found: ", len(primes), "primes")
    for i in primes:
        if not num / i % 1:
            break

    else:
        primes.append(num)
    num += 2

print(primes)
print(f"Finished in: ", time.time() - q)
