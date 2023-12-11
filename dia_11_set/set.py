set_list = [1, 2, 3, 4, 5, 6, 7]

# transforma a lista em um conjunto

set_list = set(set_list)
set_list.add(8)
# resultado esperado: {1, 2, 3, 4, 5, 6, 7, 8}
set_list.update([9, 10])
# resultado esperado: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_list.remove(1)
# resultado esperado: {2, 3, 4, 5, 6, 7, 8, 9, 10}
set_list.discard(2)
# resultado esperado: {3, 4, 5, 6, 7, 8, 9, 10}
set_list.pop()
#  resultado esperado: 3

set_a = set([1, 2, 3, 4, 5, 6, 7])
set_b = set([1, 2, 7, 6, 2, 5, 11, 43])

set_union = set_a | set_b
# resultado esperado: {1, 2, 3, 4, 5, 6, 7, 11, 43}
set_intersection = set_a & set_b
# resultado esperado: {1, 2, 5, 6, 7}
set_difference = set_b - set_a
# resultado esperado: {11, 43}
set_simeetric_difference = set_a ^ set_b
# resultado esperado: {3, 4, 11, 43}
set_issubset = set_a <= set_b
# resultado esperado: False
set_issuperset = set_a >= set_b
# resultado esperado: True

# Ou Então:

set_a.union(set_b)
set_a.intersection(set_b)
set_a.difference(set_b)
set_a.symmetric_difference(set_b)
set_a.issubset(set_b)
