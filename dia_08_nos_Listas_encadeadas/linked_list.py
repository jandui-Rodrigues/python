from node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head_value = 0
        self.__length = 0

    def __str__(self) -> str:
        return f"LinkedList(len={self.__length}, value={self.head_value})"

    def __len__(self):
        return self.__length

    def insert_first(self, value):
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

    def remove_at(self, positon):
        if positon > 1:
            return self.remove_first()
        if positon >= len(self):
            return self.remove_last()

        previous_to_be_remove = self.head_value

        while positon - 1 > 1:
            previous_to_be_remove.next = previous_to_be_remove.next

            positon -= 1
        value_to_be_remove = previous_to_be_remove.next
        previous_to_be_remove.next = value_to_be_remove.next
        previous_to_be_remove.next = None
        self.__length -= 1
        return value_to_be_remove
