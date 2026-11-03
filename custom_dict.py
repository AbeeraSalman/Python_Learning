class CustomDictionary:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def get_index(self, key):
        return hash(key) % self.capacity

    def set(self, key, value):
        index = self.get_index(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self.get_index(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        raise KeyError(key)


student = CustomDictionary()

student.set("name", "Abeera")
student.set("age", 22)

print(student.get("name"))
print(student.get("age"))