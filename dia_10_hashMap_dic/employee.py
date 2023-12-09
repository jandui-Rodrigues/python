class Employee:
    def __init__(self, id_num, name) -> None:
        self.id_num = id_num
        self.name = name


class HashMap:
    def __init__(self) -> None:
        self._buckets = [None] * 10

    def get_address(self, id_num):  # O(1)
        return id_num % 10

    def insert(self, employee):  # O(1)
        address = self.get_address(employee.id_num)
        self._buckets[address] = employee

    def update_value(self, id_num, new_value):  # O(1)
        address = self.get_address(id_num)
        employee = self._buckets[address]
        employee.name = new_value

    def get_value(self, id_num):  # O(1)
        address = self.get_address(id_num)
        return self._buckets[address]

    def has(self, id_num):  # O(1)
        address = self.get_address(id_num)
        return self._buckets[address] is not None


if __name__ == "__main__":
    employees = [(14, "name1"), (23, "name2"), (10, "name3"), (9, "name4")]
    registry = HashMap()

    for id_num, name in employees:
        employee = Employee(id_num, name)
        registry.insert(employee)

    print(registry.get_value(23))


class SeparateChaining(HashMap):
    def __init__(self) -> None:
        super().__init__()
        self._buckets = [[] for _ in range(10)]

    def insert(self, employee):  # O(1)
        address = self.get_address(employee.id_num)
        self._buckets[address].append(employee)

    def get_value(self, id_num):  # O(n)
        address = self.get_address(id_num)
        for employee in self._buckets[address]:
            if employee.id_num == id_num:
                return employee

    def update_value(self, id_num, new_value) -> None:  # O(n)
        address = self.get_address(id_num)
        for employee in self._buckets[address]:
            if employee.id_num == id_num:
                employee.name = new_value
                break
