import time


def find_prime_numbers(amount_of_primes):
    primes = [2]
    num = 3

    while len(primes) < amount_of_primes:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False

                break

        if is_prime:
            primes.append(num)

        num += 2
    return primes


amountofprimes = int(input("Amount of primes you want to find: "))

start_time = time.perf_counter()
prime_list = find_prime_numbers(amountofprimes)
end_time = time.perf_counter()
print(f"Found {len(prime_list)} prime numbers in {end_time - start_time:.5f} seconds.")
print(prime_list)
