from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self.n = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    def __len__(self) -> int:
        return len(self.n)

    def __getitem__(self, idx: int) -> Any:
        if not 0 <= idx < self.n:
            return IndexError("Index is out of bounds")
        return self.array[idx]

