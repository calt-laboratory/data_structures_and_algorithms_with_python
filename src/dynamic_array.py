class DynamicArray:
    def __init__(self) -> None:
        self._n_items = 0  # current number of items in the array
        self._array_capacity = 1
        self._array = self._create_array(array_capacity=self._array_capacity)

    def __len__(self) -> int:
        """Returns length of the array."""
        return self._n_items

    def __getitem__(self, idx: int) -> int:
        """Returns element at a given index."""
        if not 0 <= idx < self._n_items:
            raise IndexError(f"Index {idx} does not lie inside the array size of {self._n_items}")
        return self._array[idx]

    def append(self, new_item: int) -> None:
        """Appends a new element at the end of the array."""
        if self._n_items == self._array_capacity:
            new_capacity = 2 * self._array_capacity
            self._resize_array(new_capacity=new_capacity)

        self._array[self._n_items] = new_item
        self._n_items += 1
        print(f"Array: {self._array}")

    def pop(self) -> None:
        """Pops the last element of the array."""
        if self._n_items == 0:
            raise Exception("The array is empty. Pop is not possible.")

        self._array[self._n_items - 1] = None
        self._n_items -= 1
        print(f"Array: {self._array}")

        if self._n_items == self._array_capacity // 2:
            self._resize_array(new_capacity=self._array_capacity // 2)

    def insert_at(self, idx: int, new_item: int) -> None:
        """Inserts a new element at a given index and moves the subsequent elements to the right."""
        if not 0 <= idx < self._n_items:
            raise IndexError(f"Index {idx} does not lie inside the array size of {self._n_items}")

        if self._n_items == self._array_capacity:
            new_capacity = 2 * self._array_capacity
            self._resize_array(new_capacity=new_capacity)

        for i in range(self._n_items - 1, idx - 1, -1):  # Transversing backwards through the array
            self._array[i + 1] = self._array[i]

        self._array[idx] = new_item
        self._n_items += 1
        print(f"Array: {self._array}")

    def delete_at(self, idx: int) -> None:
        """Deletes an item at a given index and move the subsequent items to the left."""
        if not 0 <= idx < self._n_items:
            raise IndexError(f"Index {idx} does not lie inside the array size of {self._n_items}")

        self._array[idx] = None
        for i in range(idx + 1, self._n_items + 1):
            self._array[i - 1] = self._array[i]
        print(f"Array: {self._array}")
        self._n_items -= 1

        if self._n_items == self._array_capacity // 2:
            self._resize_array(new_capacity=self._array_capacity // 2)

    @staticmethod
    def _create_array(array_capacity: int) -> list:
        """Creates an array of given capacity (populated with None)."""
        return [None] * array_capacity

    def _resize_array(self, new_capacity: int) -> None:
        """Resizes the array to a given capacity."""
        new_array = self._create_array(array_capacity=new_capacity)

        for i in range(self._n_items):
            new_array[i] = self._array[i]

        self._array = new_array
        self._array_capacity = new_capacity
        print(f"Array: {self._array}")


def main() -> None:
    dynamic_array = DynamicArray()
    dynamic_array.append(new_item=32)
    dynamic_array.append(new_item=11)
    dynamic_array.append(new_item=22)
    dynamic_array.append(new_item=77)
    dynamic_array.insert_at(idx=2, new_item=42)
    dynamic_array.pop()
    dynamic_array.append(new_item=100)
    dynamic_array.append(new_item=55)
    dynamic_array.delete_at(idx=3)
    dynamic_array.delete_at(idx=0)
    dynamic_array.insert_at(idx=1, new_item=227)
    dynamic_array.pop()


if __name__ == "__main__":
    main()
