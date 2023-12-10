subordinates = {
    1: [2, 3],
    2: [],
    3: [4],
    4: [5, 6],
    5: [7],
    6: [],
    7: [],
}


# def score(subordinates, id) -> int:  # O(n)
#     # analize de complexidade
#     # O(n) + O(n) = O(n)
#     if subordinates[id] == []:
#         return 1
#     return 1 + sum(  # O(n)
#             [score(subordinates, sub_id) for sub_id in subordinates[id]]
#             )


def score(subordinates, id):
    # analize de complexidade Tempo
    # O(n) = O(n)
    this_score = 1
    if subordinates[id] == []:
        return this_score
    for sub_id in subordinates[id]:
        this_score += score(subordinates, sub_id)
    return this_score


print(score(subordinates, 2))
