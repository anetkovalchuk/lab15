class Element:
    def __init__(self, value: int):
        self.value: int = value
        self.next_element: 'Element | None' = None


class Chain:
    def __init__(self):
        self.start: 'Element | None' = None
        self.end: 'Element | None' = None

    def appendToEnd(self, number: int) -> None:
        new_element = Element(number)
        if self.end:
            self.end.next_element = new_element
        else:
            self.start = new_element
        self.end = new_element

    def display(self) -> None:
        current = self.start
        while current:
            print(current.value, end=' ')
            current = current.next_element
        print()

    def displayReversed(self) -> None:
        def reverse_traversal(current: 'Element | None'):
            if current is None:
                return
            reverse_traversal(current.next_element)
            print(current.value, end=' ')

        reverse_traversal(self.start)
        print()


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        total = int(file.readline().strip())
        numbers = list(map(int, file.readline().split()))

    chain = Chain()
    for number in numbers:
        chain.appendToEnd(number)

    chain.display()
    chain.displayReversed()
