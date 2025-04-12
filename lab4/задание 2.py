import math

def prime_numbers():
    yield 2
    primes = [2]
    num = 3

    while True:
        is_prime = True
        sqrt_num = math.sqrt(num)

        for p in primes:
            if p > sqrt_num:
                break
            if num % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            yield num

        num += 2
def get_user_input():
    while True:
        try:
            limit = int(input("Введите верхнюю границу для поиска простых чисел (>1): "))
            if limit < 2:
                print("Число должно быть больше 1!")
                continue
            return limit
        except ValueError:
            print("Введите целое число!")


def main():
    limit = get_user_input()
    print(f"\nПростые числа до {limit} включительно:")

    prime_gen = prime_numbers()
    for prime in prime_gen:
        if prime > limit:
            break
        print(prime)

main()