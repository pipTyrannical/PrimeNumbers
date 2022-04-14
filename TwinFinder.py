import time

primes = [2]
twins = []
lastprime = 2
num = 3


amountofprimes = int(input("Amount of twin primes you want to find: "))

q = time.time()
while len(twins) < amountofprimes:
    print("Found:", len(twins), "twin primes")
    for i in primes:
        if not num / i % 1:
            break

    else:
        primes.append(num)
        if num == lastprime + 2:
            twins.append([lastprime, num])

        lastprime = num
    num += 2

print(twins)
print(f"Finished in: ", time.time() - q)
input()
