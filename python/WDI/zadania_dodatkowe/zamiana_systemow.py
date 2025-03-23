def zamiana_systmow(n, system):
    result = 0
    multiplier = 1  # Potrzebujemy mnożnika, aby poprawnie złożyć wynik

    while n > 0:
        result += (n % system) * multiplier
        n //= system
        multiplier *= 10  # Przesuwamy miejsce dziesiętne na kolejną cyfrę w wyniku

    return result


print(zamiana_systmow(1423523, 16))