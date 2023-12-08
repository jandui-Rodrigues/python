from double_list import DoubleNode
from rich import print


class LinkDouble:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__length = 0

    def __str__(self) -> str:
        str_items = ""
        element = self.head
        for i in range(len(self) + 1):
            str_items += str(element.value)
            element = element.next
            if i + 1 <= len(self):
                str_items += ", "

        return "LinkDouble(" + str_items + ")"

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        new_value = DoubleNode(value)
        if self.head is None:  # Se a lista está vazia
            self.head = new_value
            self.tail = new_value
            return
        new_value.next = self.head
        self.head.previous = new_value
        self.head = new_value

        self.__length += 1

    def insert_last(self, value):
        current = self.head
        if current is None:
            return self.insert_first(value)
        new_tail = DoubleNode(value)
        self.tail.next = new_tail
        new_tail.previous = self.tail
        self.tail = new_tail
        self.__length += 1

    def insert_at(self, value, positon):
        if positon < 1:
            return self.insert_first(value)
        if positon >= len(self):
            return self.inset_last(value)
        new_value = DoubleNode(value)
        current = self.head
        while positon > 1:
            current = current.next
            positon - 1
        new_value.next = current.next
        new_value.previous = current
        current.next = new_value
        current.next.previous = new_value
        self.__length += 1

    def remove_first(self):
        value_to_be_removed = self.head
        if value_to_be_removed:
            self.head = self.head.next
            self.head.previous = None
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()
        value_to_remove = self.tail
        previous_to_remove = value_to_remove.previous
        previous_to_remove.next = None
        self.tail.previous = None
        self.tail = previous_to_remove
        self.__length -= 1

        return value_to_remove

    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self.head

        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
            if value_to_be_returned:
                value_returned = DoubleNode(value_to_be_returned.value)
        return value_returned


if __name__ == "__main__":
    listed = LinkDouble()
    listed.insert_first(1)
    listed.insert_first(2)
    listed.insert_last(10)
    listed.insert_at(5, 1)
    print(listed)
