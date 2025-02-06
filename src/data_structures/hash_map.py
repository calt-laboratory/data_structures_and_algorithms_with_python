from typing import Any, Type


class HashMap:
    def __init__(self, size: int) -> None:
        self.size = size
        self.hash_map = [(None, ) for _ in range(self.size)]

    def _hash_function(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int | float | str) -> None:
        # Convert/Compute a hashed key (index) from the key
        idx = self._hash_function(key=key)

        if self.hash_map[idx][0] is None:
            self.hash_map[idx] = (key, value)
            return

        # Loop through map if there is already a key at position idx
        if self.hash_map[idx][0] != key:
            for i, pair in enumerate(self.hash_map[idx + 1:], start=idx + 1):
                if pair[0] is None:
                    self.hash_map[i] = (key, value)
                    return
        return

    def get(self, key: int) -> Type[KeyError] | Any:

        idx = self._hash_function(key=key)

        if key == self.hash_map[idx][0]:
            return self.hash_map[idx][1]

        if key is None:
            return KeyError

        for pair in self.hash_map[idx + 1:]:
            if key == pair[0]:
                return pair[1]

    def __str__(self) -> str:
        return str([item for item in self.hash_map])

    def __len__(self) -> int:
        return len(self.hash_map)


def main() -> None:
    hash_map = HashMap(size=10)
    print(hash_map)
    # print(len(hash_map))
    hash_map.put(key=42, value="Douglas Adams")
    print(hash_map)
    hash_map.put(key=24, value="NOT")
    print(hash_map)
    hash_map.put(key=11, value="Eleven")
    print(hash_map)
    hash_map.put(key=22, value="Twenty Two")
    print(hash_map)
    print(hash_map.get(key=22))
    print(hash_map.get(key=11))
    print(hash_map.get(key=24))
    print(hash_map.get(key=42))
    print(hash_map.get(key=11111))


if __name__ == "__main__":
    main()
