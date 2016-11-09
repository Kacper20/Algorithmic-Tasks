"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    temp_a = headA
    temp_b = headB
    while not temp_a is temp_b:
        if temp_a.next is None:
            temp_a = headB
        else:
            temp_a = temp_a.next
        if temp_b.next is None:
            temp_b = headA
        else:
            temp_b = temp_b.next
    return temp_a.data
  
  
  
  
  
  
  
  
  

