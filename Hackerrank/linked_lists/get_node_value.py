#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""


def GetNode(head, position):
    counter = 0
    slow = head
    fast = head
    while counter != position:
        fast = fast.next
        counter += 1
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    return slow.data


  
  
  
  
  
  
  
  
  

