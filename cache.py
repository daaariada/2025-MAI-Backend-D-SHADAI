class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: str) -> str:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return ''

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest_key = self.order.pop(0)
            del self.cache[oldest_key]
        self.cache[key] = value
        self.order.append(key)

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
            self.order.remove(key)
