
class Stack[T]:
    def __init__(self) -> None:
        self.items = []

    def __len__(self) -> int:
        return len(self.items)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("pop() called on empty stack")
        self.items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek() called on empty stack")
        return self.items[-1]

    def is_empty(self) -> bool:
        return self.items == []


def main() -> None:
    stack = Stack()
    print(stack.is_empty())
    print(len(stack))
    stack.push("noise")
    print(stack.peek())
    stack.push("science")
    print(stack.peek())
    stack.push(42)
    print(stack.peek())
    print(stack.is_empty())
    print(len(stack))
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.is_empty())


if __name__ == "__main__":
    main()
