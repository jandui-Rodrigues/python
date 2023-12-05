class DoubleNode:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self) -> str:
        return f"V: { self.value}, N: {self.next} P: {self.previous}"

    def reset(self):
        self.next: None
        self.previous = None
