class Node:
    def __init__(self, message):
        self.message = message
        self.right_node = None
        self.left_node = None

    def add_message(self, new_message, option, old_message):
        if self.message == old_message:
            if option == "right":
                self.right_node = Node(new_message)
            else:
                self.left_node = Node(new_message)
        else:
            if self.right_node != None:
                self.right_node.add_message(new_message, option, old_message)
            if self.left_node != None:
                self.left_node.add_message(new_message, option, old_message)


class Discusion_tree:
    def __init__(self):
        self.first_node = None
        self.current_conversation_node = None

    def add_first_message(self, message):
        self.first_node = Node(message)
        self.current_conversation_node = self.first_node


    def add_message(self, new_message, option, old_message):
        self.first_node.add_message(new_message, option, old_message)

    def next_message(self, option):
        if self.current_conversation_node == None:
            if option == "right":
                self.current_conversation_node = self.first_node.right_node
            elif option == "left":
                self.current_conversation_node = self.first_node.left_node
        else:
            if option == "right":
                self.current_conversation_node = self.current_conversation_node.right_node
            elif option == "left":
                self.current_conversation_node = self.current_conversation_node.left_node

    def show_message(self):
        if self.current_conversation_node == None:
            return "FIN DE L'ARBRE"
        return self.current_conversation_node.message
    
    def isLastMessage(self):
        if self.current_conversation_node.left_node==None and self.current_conversation_node.right_node==None:
            return True
        else:
            return False


# Discusion = Discusion_tree()
# Discusion.first_node = Node("Help?")
# Discusion.add_message("Python ?", "right", "Help?")
# Discusion.add_message("tant pis", "left", "Help?")
# Discusion.next_message("right")
# Discusion.next_message("left")
# print(Discusion.show_message())
