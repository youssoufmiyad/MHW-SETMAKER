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
        
        for i in range(len(bucket)-1):
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
        
    
avancement_conversation=Hashmap(2)
avancement_conversation.set("utilisateurs",[])
avancement_conversation.set("message",[])
