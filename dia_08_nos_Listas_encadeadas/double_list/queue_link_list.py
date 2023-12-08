from link_double import LinkDouble


class Queue:
    def __init__(self) -> None:
        self.data = LinkDouble()

    def is_empty(self):
        return not len(self.__data)

    def enqueue(self, value):
        self.data.insert_last(value)

    def dequeue(self):
        return self.data.remove_first()

    def peek(self):
        return self.data.get_element_at(0)


node = LinkDouble()
node.insert_first(1)

print(node.get_element_at(0))
