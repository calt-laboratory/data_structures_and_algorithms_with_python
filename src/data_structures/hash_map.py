from typing import Optional


class HashMap:
    def __init__(self, size: int) -> None:
        self.size = size
        self.hash_map_keys: list[Optional[int]] = [None] * self.size
        self.hash_map_values: list[Optional[int]] = [None] * self.size


    def _hash_function(self, key: int) -> int:
        return key % self.size

    def rehash_by_open_addressing(self, old_hash: int) -> int:
        return (old_hash + 1) % self.size

    def put(self, key: int, value: int) -> None:
        # Convert/Compute a hashed key (index) from the key
        idx = self._hash_function(key=key)

        if self.hash_map_keys[idx] is None:
            self.hash_map_keys[idx] = key
            self.hash_map_values[idx] = value
            return

        if self.hash_map_keys[idx] == key:
            pass


    def __len__(self) -> int:
        return len(self.hash_map_keys)


def main() -> None:
    hm = HashMap(size=10)
    print(hm)
    print(len(hm))


if __name__ == "__main__":
    main()
