from link_double import LinkDouble


class Stack:
    def __init__(self) -> None:
        self._data = LinkDouble()

    def is_empty(self):
        return not len(self)

    def push(self, value):
        self._data.insert_last(value)

    def pop(self):
        return self._data.remove_last()

    def peek(self):
        return self._data.get_element_at(len(self))

    def min_value(self):
        if self.is_empty():
            return None

        min = self._data.get_element_at(1)
        min_sencond = self._data.get_element_at(0)
        min_value = 0

        for index in range(len(self._data)):
            if min > min_sencond:
                min_value = min
            min_value = self._data.get_element_at(index)
            min_sencond = self._data.get_element_at(index + 1)
        return min_value
