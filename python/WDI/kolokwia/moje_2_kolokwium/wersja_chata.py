def to_base_5(n):
    """Konwertuje liczbę n na system o podstawie 5 i zwraca zbiór cyfr."""
    digits = set()
    while n > 0:
        digits.add(n % 5)
        n //= 5
    return digits

def neighbors(x, y, N):
    """Zwraca listę współrzędnych sąsiednich pól w odległości 1 lub 2 ruchów króla."""
    directions = [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
                  (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
                  (0, -2), (0, -1), (0, 1), (0, 2),
                  (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
                  (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]
    return [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < N and 0 <= y + dy < N]

def is_lucky(T, x, y, N):
    """Sprawdza, czy pole (x, y) jest szczęśliwe."""
    target_digits = to_base_5(T[x][y])
    lucky_neighbors_count = 0
    for nx, ny in neighbors(x, y, N):
        if to_base_5(T[nx][ny]) == target_digits:
            lucky_neighbors_count += 1
    return lucky_neighbors_count == 17

def luck17(T):
    """Sprawdza, czy w jakimkolwiek wierszu lub kolumnie znajduje się więcej niż jedno szczęśliwe pole."""
    N = len(T)
    for i in range(N):
        # Sprawdzamy wiersz
        lucky_in_row = sum(is_lucky(T, i, j, N) for j in range(N))
        if lucky_in_row > 1:
            return True
        
        # Sprawdzamy kolumnę
        lucky_in_col = sum(is_lucky(T, j, i, N) for j in range(N))
        if lucky_in_col > 1:
            return True
    
    return False

T = [
    [5, 5, 5, 5],
    [5, 5, 5, 5],
    [5, 5, 5, 5],
    [5, 5, 5, 5]
]
print(luck17(T))  # Przykładowe testy