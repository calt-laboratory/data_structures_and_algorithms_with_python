from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._current_number_of_elements = 0
        self._array_capacity = 1
        self._array = self._create_array(array_capacity=self._array_capacity)

    def __len__(self) -> int:
        return self._current_number_of_elements

    def __getitem__(self, idx: int) -> Any:
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

    def pop(self) -> None:
        """Pops the last element of the array."""
        if self._current_number_of_elements == 0:
            print("The array is empty.")
        self._array[self._current_number_of_elements - 1] = None
        self._current_number_of_elements -= 1

    @staticmethod
    def _create_array(array_capacity: int) -> list:
        return [None] * array_capacity

    def _resize_array(self, new_capacity: int) -> None:
        new_array = self._create_array(array_capacity=new_capacity)
        for i in range(self._current_number_of_elements):
            new_array[i] = self._array[i]
        self._array = new_array
        self._array_capacity = new_capacity


def main() -> None:
    dynamic_array = DynamicArray()
    dynamic_array.append(new_element=100)
    dynamic_array.append(new_element=24)
    print(dynamic_array[0])
    print(dynamic_array[1])
    print(len(dynamic_array))
    dynamic_array.pop()
    print(len(dynamic_array))
    print(dynamic_array[1])


if __name__ == "__main__":
    main()
