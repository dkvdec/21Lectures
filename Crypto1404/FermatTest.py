import sys
import math

def main(num):
    print("Сгенерируем определенное количество чисел a, взаимопростых с данным числом num")
    primes = [2, 3, 5, 7, 11, 13,
              109, 113, 127, 191,
              193, 197, 199]
    for i in primes:
        if num % i == 0:
            continue
        print("Проверяем {}^({} - 1): Остаток от деления данного числа на {} == {}".format(i, num, num, (i ** (num - 1) % num)))
        if (i ** (num - 1) % num) != 1:
            print("Тест простоты Ферма не пройден. Число гарантировано не простое.")
            sys.exit()
    if (num in [561, 41041, 825265, 321197185, 5394826801]):
        print("Число не простое, однако проходит все тесты простоты Ферма.")
        print("Такие числа называются числами Кармайкла.")
    else:
        print("Число {} простое с определенной вероятностью.".format(num))

#try:
main(int(sys.argv[1]))
#except Exception as e:
 #   print("usage: python3 [num]")
