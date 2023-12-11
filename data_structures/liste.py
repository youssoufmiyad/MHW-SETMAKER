class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class chained_list:
    def __init__(self):
        self.first_node = None
        
    def clear_list(self):
        self.first_node = None
        
    def append(self,data):
        
        if self.first_node == None:
            self.first_node=Node(data)
            return
        
        current_node = self.first_node
        while current_node.next_node != None:
            current_node = current_node.next_node
            
        new_node = Node(data)
        current_node.next_node = new_node
        
    def lenght(self):
        if self.first_node==None:
            return 0
        count = 0
        current_node = self.first_node
        while current_node != None:
            current_node = current_node.next_node
            count+= 1

            
        return count
    
    def search(self,data):
        isHere = False
        
        if self.first_node == None:
            raise Exception("empty list")
        
        current_node = self.first_node
        
        while current_node != None:
            if current_node.data == data:
                isHere = True
                return isHere
            current_node=current_node.next_node
        return isHere
    
    def get(self,index):
        if index==0:
            if self.first_node!=None:
                return self.first_node.data
        elif self.first_node == None:
            raise Exception("empty list")
        else:        
            current_node = self.first_node

            for i in range(index+1):
                if i == index:
                    if current_node.data != None:
                        return current_node.data
                elif current_node.next_node == None:
                    raise Exception("out of range")
                current_node = current_node.next_node
                
    def insert(self, data, index):
        current_node = self.first_node
        i = 1
        while i < index:
            current_node = current_node.next_node
            i+=1

        new_node = Node(data)
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
                
    
# L = chained_list()
# L.append(5)
# L.append(8)
# L.append(10)
# L.append(18)

# print("lenght : ",L.lenght()," search(8) : ",L.search(8)," search(9) : ",L.search(9)," get(0) : ",L.get(0)," get(L.length()-1) : ",L.get(L.lenght()-1))
# print("Nodes :")
# for i in range(L.lenght()):
#     print(L.get(i))
# L.insert(25,2)
# print("new length : ",L.lenght())
# print("Nodes :")
# for i in range(L.lenght()):
#     print(L.get(i))