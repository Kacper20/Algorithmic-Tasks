"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if headA is None:
        return headB
    elif headB is None:
        return headB
    elif headA is None and headB is None:
        return None
    temp_a = headA
    temp_b = headB
    new_head = None
    if temp_b.data < temp_a.data:
        new_head = temp_b
        temp_b = temp_b.next
    else:
        new_head = temp_a
        temp_a = temp_a.next
        
    temp = new_head
    while temp_a is not None and temp_b is not None:
        next = None
        if temp_a.data < temp_b.data:
            next = temp_a
            temp_a = temp_a.next
        else:
            next = temp_b
            temp_b = temp_b.next
        temp.next = next
        temp = temp.next
    leftover = None
    if temp_b is not None:
        leftover = temp_b
    else:
        leftover = temp_a
    while leftover is not None:
        temp.next = leftover
        temp = temp.next
        leftover = leftover.next  
    return new_head
  
  
  
  
  
  
  
  
  
  

