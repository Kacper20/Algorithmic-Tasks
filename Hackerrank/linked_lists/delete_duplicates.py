"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head is None:
        return head
    temp = head
    while temp is not None:
        if temp.next is not None and temp.next.data is temp.data:
            new_temp = temp.next
            while new_temp is not None and new_temp.data is temp.data:
                new_temp = new_temp.next
            temp.next = new_temp
        else:
            temp = temp.next
    return head
  
  
  
  
  
  
  
  
  
  

