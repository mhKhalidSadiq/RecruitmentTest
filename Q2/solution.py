#Written By: Khalid Sadiq (AI Engineer)
#Dated : 27/09/2022

#Class for creating new node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Class for linked list with required functionality    
class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and make linked list
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

  # Remove Nth element from End
    def deleteNode(self, n):
        first = self.head
        second = self.head

    # Moving first pointer n steps ahead of second pointer
        for i in range(n):
            
            # If count of nodes in the
            # given list is less than 'n'
            if(first.next == None):
                
                # If index = n then
                # delete the head node
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            first = first.next
        
    #Now moving first pointer till end and moving second pointer which is n steps back from first
        while(first.next != None):
            first = first.next
            second = second.next
        # Now seconds pointer is exactlyt at the node which needs to be deleted
        second.next = second.next.next
    
  # Print Linked List 
    def printList(self):
        tmp_head = self.head
        while(tmp_head != None):
            print(tmp_head.value, end = ' ')
            tmp_head = tmp_head.next
        
# Creating Linked List
linked_list = LinkedList()
# Inserting values one by one
linked_list.insert(5)
linked_list.insert(4)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)
print("Created Linked list is: ")
linked_list.printList()
n=2
linked_list.deleteNode(n) # Deleting node
print("\nLinked List after Deletion is: ")
linked_list.printList()

#Output
"""
Created Linked list is: 
1 2 3 4 5 
Linked List after Deletion is: 
1 2 3 5 
"""
