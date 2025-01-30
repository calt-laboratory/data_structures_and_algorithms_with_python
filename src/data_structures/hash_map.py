from typing import Optional


class HashMap:
    def __init__(self, size: int) -> None:
        self.size = size
        self.hash_map: list[Optional[int]] = [None] * self.size


    def _hash_function(self, key: int) -> int:
        return key % self.size

    def rehash_by_open_addressing(self, old_hash: int) -> int:
        return (old_hash + 1) % self.size

    def put(self, key: int, value: int | float | str) -> None:
        # Convert/Compute a hashed key (index) from the key
        idx = self._hash_function(key=key)

        if self.hash_map[idx] is None:
            self.hash_map[idx] = (key, value)
            return None

        if self.hash_map[idx][0] != key:
            for i, pair in enumerate(self.hash_map):
                if pair is None:
                    self.hash_map[i] = (key, value)
                    return None

        return None

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


if __name__ == "__main__":
    main()
