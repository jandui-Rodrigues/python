from node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head_value = None
        self.__length: int = 0

    def __str__(self) -> str:
        return f"LinkedList(len={self.__length}, value={self.head_value})"

    def __len__(self) -> int:
        return self.__length

    def insert_first(self, value) -> None:
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def insert_last(self, value):
        last_value = Node(value)
        current_value = self.head_value

        if current_value is None:
            return self.insert_first(value)

        while current_value.next:
            current_value = current_value.next

        current_value.next = last_value
        self.__length += 1

    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        current_value = self.head_value
        while position > 1:
            current_value = current_value.next
            position -= 1
        next_value = Node(value)
        next_value.next = current_value.next
        current_value.next = next_value
        self.__length += 1

    def remove_first(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed

    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()

        last = self.__length
        previous_to_be_remove = self.head_value
        index = 0
        while index < last - 1:
            previous_to_be_remove.next = previous_to_be_remove.next
            index += 1
        value_to_be_removed = previous_to_be_remove.next
        previous_to_be_remove.next = None
        self.__length -= 1
        return value_to_be_removed

    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self.head_value
        while position > 1:
            previous_to_be_removed = previous_to_be_removed.next
            position -= 1
        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next = None
        self.__length -= 1
        return value_to_be_removed

    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self.head_value

        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
            if value_to_be_returned:
                value_returned = Node(value_to_be_returned.value)
        return value_returned

    def is_empty(self):
        return not self.__length


if __name__ == "__main__":
    linked_list = LinkedList()

    print(linked_list.is_empty())
    linked_list.insert_first(1)
    print(linked_list)

    linked_list.insert_first(2)
    linked_list.insert_first(5)
    print(
        linked_list
    )
    print(linked_list.get_element_at(0))
    print(linked_list.get_element_at(1))
    print(linked_list.get_element_at(2))
