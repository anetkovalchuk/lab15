class Element:
    def __init__(self, value: int):
        self.value: int = value
        self.next_element: 'Element | None' = None


class Chain:
    def __init__(self):
        self.first: 'Element | None' = None
        self.last: 'Element | None' = None

    def appendToEnd(self, num: int) -> None:
        element = Element(num)
        if not self.first:
            self.first = self.last = element
        else:
            self.last.next_element = element
            self.last = element

    def shiftRight(self, steps: int) -> None:
        if not self.first or not self.first.next_element or steps == 0:
            return
        length = 1
        current = self.first
        while current.next_element:
            current = current.next_element
            length += 1
        current.next_element = self.first
        steps = steps % length
        if steps == 0:
            current.next_element = None
            return
        move_to_new_end = length - steps
        new_end = self.first
        for _ in range(move_to_new_end - 1):
            new_end = new_end.next_element
        self.first = new_end.next_element
        new_end.next_element = None

    def display(self) -> None:
        current = self.first
        result = []
        while current:
            result.append(str(current.value))
            current = current.next_element
        print(" ".join(result))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file if line.strip()]
    if len(lines) < 2:
        exit()
    try:
        count = int(lines[0])
        if count < 1:
            exit()
        values = list(map(int, lines[1].split()))
        if len(values) != count:
            exit()
        rotations = list(map(int, lines[2:]))
    except ValueError:
        exit()
    chain = Chain()
    for value in values:
        chain.appendToEnd(value)
    for rotation in rotations:
        if rotation < 0:
            continue
        chain.shiftRight(rotation)
        chain.display()
