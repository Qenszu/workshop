from zad6testy import runtests
from queue import PriorityQueue

def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje

    return None


G = [   [0, 1, 200, 200, 200, 200],
        [1, 0, 2, 200, 200, 200],
        [200, 2, 0, 40, 200, 200],
        [200, 200, 40, 0, 40, 200],
        [200, 200, 200, 40, 0, 117],
        [200, 200, 200, 200, 117, 0]]

print(jumper(G, 0, 5))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( jumper, all_tests = False )