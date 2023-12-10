"""
2- Escreva um método para incluir uma nova pessoa na equipe de uma outra
 pessoa.
 Seu método deve considerar que cada pessoa pode ter no máximo k pessoas em seu
 time. Se o time estiver cheio, a nova contratada pode ser alocada na equipe
 de qualquer pessoa abaixo dela, não precisando ser na equipe
 imediatamente abaixo.
"""


class HierarchyInsert:
    def __init__(self, k):
        self.k = k
        self.subordinates = {}
        self.scores = {}

    def insert(self, id, new_id):
        if not id:
            self.subordinates[new_id] = []
            self.scores[new_id] = 1
            return

        self.scores[id] += 1

        if len(self.subordinates[id]) < self.k:
            self.subordinates[id].append(new_id)
            self.subordinates[new_id] = []
            self.scores[new_id] = 1
        else:
            self.insert(self.subordinates[id][0], new_id)

    def get_score(self, id):
        # self.score(id)
        # print(f" o valor para o {id} é: {self.scores[id]}")
        print(self.score(id))


hierarchy_insert = HierarchyInsert(2)

hierarchy_insert.insert(None, 1)
hierarchy_insert.insert(1, 2)
hierarchy_insert.insert(1, 3)
hierarchy_insert.insert(2, 4)
hierarchy_insert.insert(4, 5)
hierarchy_insert.insert(4, 6)
hierarchy_insert.insert(5, 7)

hierarchy_insert.get_score(1)
