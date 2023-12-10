"""
Caso a empresa precise fazer essa consulta frequentemente, como você pode
tornar essas consultas mais eficientes? Como você pode guardar o resultado
de consultas anteriores?
"""


class Hierarchy:
    def __init__(self, subordinates):
        self.subordinates = subordinates
        self.scores = {}

    def get_score(self, id):
        self.score(id)
        print(f" o valor para o {id} é: {self.scores[id]}")
        # return self.scores[id]

    def score(self, id):
        this_score = 1
        if self.subordinates[id] == []:
            self.scores[id] = this_score
            return this_score
        for sub_id in self.subordinates[id]:
            this_score += self.score(sub_id)

        self.scores[id] = this_score
        return this_score


subordinates = {
    1: [2, 3],
    2: [],
    3: [4],
    4: [5, 6],
    5: [7],
    6: [],
    7: [],
}

hierarchy = Hierarchy(subordinates)

hierarchy.get_score(2)
hierarchy.get_score(3)
hierarchy.get_score(1)
