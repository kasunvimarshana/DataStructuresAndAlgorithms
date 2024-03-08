class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
         
    def hash_function(self, key):
        return hash(key) % self.size
     
    def set_value(self, key, value):
        index = self.hash_function(key)
        found = False
        for i, kv in enumerate(self.buckets[index]):
            k, v = kv
            if key == k:
                self.buckets[index][i] = (key, value)
                found = True
                break
        if not found:
            self.buckets[index].append((key, value))
     
    def get_value(self, key):
        index = self.hash_function(key)
        for k, v in self.buckets[index]:
            if key == k:
                return v
        return None