from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._current_number_of_elements = 0
        self._array_capacity = 1
        self._array = self._create_array(array_capacity=self._array_capacity)

    def __len__(self) -> int:
        """Returns length of the array."""
        return self._current_number_of_elements

    def __getitem__(self, idx: int) -> Any:
        """Returns element at a given index."""
        if not 0 <= idx < self._current_number_of_elements:
            raise IndexError(f"Index {idx} does not lie inside the array size of {self._current_number_of_elements}")
        return self._array[idx]

    def append(self, new_element: Any) -> list:
        """Appends a new element at the end of the array."""
        if self._current_number_of_elements == self._array_capacity:
            new_capacity = 2 * self._array_capacity
            self._resize_array(new_capacity=new_capacity)

        self._array[self._current_number_of_elements] = new_element
        self._current_number_of_elements += 1
        print(f"Array: {self._array}")

    def pop(self) -> None:
        """Pops the last element of the array."""
        if self._current_number_of_elements == 0:
            raise Exception("The array is empty. Pop is not possible.")

        self._array[self._current_number_of_elements - 1] = None
        self._current_number_of_elements -= 1
        print(f"Array: {self._array}")

    def insert_at(self, idx: int, new_element: Any) -> None:
        """Inserts a new element at a given index and moves the subsequent elements to the right."""
        if not 0 <= idx < self._current_number_of_elements:
            raise IndexError(f"Index {idx} does not lie inside the array size of {self._current_number_of_elements}")

        if self._current_number_of_elements == self._array_capacity:
            new_capacity = 2 * self._array_capacity
            self._resize_array(new_capacity=new_capacity)

        # Transversing backwards through the array
        for i in range(self._current_number_of_elements - 1, idx - 1, -1):
            self._array[i + 1] = self._array[i]

        self._array[idx] = new_element
        self._current_number_of_elements += 1
        print(f"Array: {self._array}")

    @staticmethod
    def _create_array(array_capacity: int) -> list:
        """Creates an array of given capacity (populated with None)."""
        return [None] * array_capacity

    def _resize_array(self, new_capacity: int) -> None:
        """Resizes the array to a given capacity."""
        new_array = self._create_array(array_capacity=new_capacity)

        for i in range(self._current_number_of_elements):
            new_array[i] = self._array[i]

        self._array = new_array
        self._array_capacity = new_capacity
        print(f"Array capacity: {self._array_capacity}")


def main() -> None:
    dynamic_array = DynamicArray()
    dynamic_array.append(new_element=32)
    dynamic_array.append(new_element=11)
    dynamic_array.append(new_element=22)
    dynamic_array.append(new_element=77)
    dynamic_array.insert_at(idx=2, new_element=111)
    dynamic_array.pop()


if __name__ == "__main__":
    main()
