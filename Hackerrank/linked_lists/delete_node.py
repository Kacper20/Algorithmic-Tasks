"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if position == 0:
        return head.next
    counter = 0
    temp = head
    while counter + 1 != position:
        temp = temp.next
        counter += 1 
    if temp.next is not None:
        temp.next = temp.next.next
    else:
        temp.next = None
    return head
    
  
  
  
  
  

