numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for elem in numbers :
    is_prime = True
    for divisor in range(2, elem) :
        if elem % divisor == 0 :
            not_primes.append(elem)
            is_prime = False
            break

    if is_prime == True and elem != 1:
        primes.append(elem)
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")



