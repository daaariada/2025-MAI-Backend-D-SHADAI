class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache = {}

    def get(self, key: str) -> str:
        if key in self.cache:
            return self.cache[key]
        else:
            return ''

    def set(self, key: str, value: str) -> None:
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))
        else:
            self.cache.update({key: value})

    def rem(self, key: str) -> None:
        del self.cache[key]
