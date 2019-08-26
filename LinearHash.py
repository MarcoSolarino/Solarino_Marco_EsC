
class LinearHash:
    def __init__(self, m):
        self.m = m
        self.hash = {}
        self.collision = 0
        for i in range(m):
            self.hash[i] = None

    def linear_insert(self, k):
        i = 0
        while i != self.m:
            key = ((k % self.m) + i) % self.m
            if (self.hash[key] is None) or (self.hash[key] == "DELETED"):
                self.hash[key] = k
                return key
            else:
                i += 1
                self.collision += 1
        #print("tabella piena")

    def linear_search(self, k):
        i = 0
        while i != self.m:
            key = ((k % self.m) + i) % self.m
            if self.hash[key] == k:
                return k
            elif self.hash[key] is None:
                return None
            i += 1
        return None


    def linear_delete(self, k):
        key = self.linear_search(k)
        if key is not None:
            self.hash[key] = "DELETED"
            self.collision -= 1
