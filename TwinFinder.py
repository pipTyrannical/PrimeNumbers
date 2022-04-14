import time

twins = []
lastprime = 2
num = 3


amountofprimes = int(input("Amount of twin primes you want to find: "))

q = time.time()
while len(primes) < amountofprimes:
    print("Found: ", len(primes), "primes")
    for i in primes:
        if not num / i % 1:
            break

    else:
        if num == lastprime + 2:
            twins.append([lastprime, num])

        lastprime = num
    num += 2

print(twins)
print(f"Finished in: ", time.time() - q)
