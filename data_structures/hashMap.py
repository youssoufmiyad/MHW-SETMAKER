class Hashmap:
    def __init__(self,size):
        self.size = size
        self.buckets = []
        for i in range(size):
            self.buckets.append([])
        
    def set(self,key,value):
        hashed_key = hash(key)
        idx = hashed_key % self.size
        
        bucket = self.buckets[idx]
        
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
        
        self.buckets[idx].append((key,value))

    
    def get(self,key):
        hashed_key = hash(key)
        idx = hashed_key % self.size
        bucket = self.buckets[idx]
        for k,v in bucket:
            if k == key:
                return v
        
    
        
h = Hashmap(5)
h.set(9,17)
print(h.get(9))

h.set("test",24)
print(h.get("test"))

h.set(9,18)
print(h.get(9))

print(h.buckets)