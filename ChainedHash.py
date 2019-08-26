
class ChainedHash:
    def __init__(self, m):
        self.m = m
        self.hash = {}
        self.collision = 0
        for i in range(m):
            self.hash[i] = []

    def insert(self, k):
        key = k % self.m
        self.hash[key].append(k)

    def chained_search(self, k):
        key = k % self.m
        for x in self.hash[key]:
            if x == k:
                return x
        return None


    def delete_chained(self, k):
        key = k % self.m
        element = self.chained_search(k)
        if element is not None:
            self.hash[key].remove(element)

    def calculate_collision(self):
        for i in range(self.m):
            if len(self.hash[i]) != 0:
                self.collision += (len(self.hash[i]) - 1)
