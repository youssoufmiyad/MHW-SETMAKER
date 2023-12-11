class Node :
  def __init__(self, message):
    self.message = message
    self.yes_node = None
    self.no_node = None

  def add_message(self, new_message, yes_or_no, old_message ):
    if self.message == old_message :
      if yes_or_no == "oui":
        self.yes_node = Node(new_message)
      else:
        self.no_node = Node(new_message)
    else:
      if self.yes_node != None:
        self.yes_node.add_message(new_message, yes_or_no, old_message )
      if self.no_node != None:
        self.no_node.add_message(new_message, yes_or_no, old_message )

class Discusion_tree:
  def __init__(self):
    self.first_node = None
    self.current_conversation_node = None

    def next_message(self, yes_or_no):
        if yes_or_no == "oui":
            self.current_conversation_node = self.current_conversation_node.yes_node
        elif yes_or_no == "non":
            self.current_conversation_node = self.current_conversation_node.no_node
        

  def add_message(self, new_message, yes_or_no, old_message ):
    self.first_node.add_message(new_message, yes_or_no, old_message)
    
Discusion = Discusion_tree()
Discusion.first_node = Node("Help?")
Discusion.add_message("Python ?","oui","Help?")
Discusion.add_message("tant pis","non","Help?")
