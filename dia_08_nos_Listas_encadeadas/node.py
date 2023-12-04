class Node:
    def __init__(self, list) -> None:
        self.list = list
        self.next = None

    def __str__(self):
        return f" Node(list data = {self.list}), next = { self.next}"
