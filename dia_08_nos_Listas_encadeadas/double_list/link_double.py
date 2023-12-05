from double_list import DoubleNode


class LinkDouble:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__length = 0

    def __str__(self) -> str:
        return f"LinkedList(len={self.__length}, value={self.head.value})"

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        new_value = DoubleNode(value)
        if self.head is None:  # Se a lista está vazia
            self.head = new_value
            self.tail = new_value
        else:
            new_value.next = self.head
            self.head.previous = new_value
            self.head = new_value

        self.__length += 1


listed = LinkDouble()
listed.insert_first(1)
listed.insert_first(2)

print(listed)
