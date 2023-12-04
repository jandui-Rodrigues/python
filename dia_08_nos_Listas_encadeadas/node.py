class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return f" Node(value data = {self.value}), next = { self.next}"
