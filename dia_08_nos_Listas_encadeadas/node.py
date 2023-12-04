class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previus = None

    def __str__(self):
        return f"{self.value} next = {self.next}, previus = {self.previus}"
