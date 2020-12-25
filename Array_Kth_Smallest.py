#Kth smallest element in an array
from linkedList import linkedList,Node
from quickSearch import KthSmallest

class myLinkedList(linkedList):
	def leftElement(self):
		return self.root.next.data

	def correctInsertion(self, data):
		newNode = Node(data)
		current_node = self.root.next
		previous_node = self.root
		while(current_node.next!= None and current_node.data > data):
			previous_node = current_node
			current_node = current_node.next
		previous_node.next = newNode
		newNode.next = current_node		
		self.length +=1

def linkedListMethod(array,k):	
	my_linked_list = myLinkedList()
	for i in array:
		if my_linked_list.getLength() == 0:
			my_linked_list.addElementToLeft(i)
		elif i < my_linked_list.leftElement():
			my_linked_list.correctInsertion(i)
			if my_linked_list.getLength() > k:
				my_linked_list.deleteFirstElement()
		elif i > my_linked_list.leftElement():
			if my_linked_list.getLength() < k:
				my_linked_list.addElementToLeft(i)
	#my_linked_list.traverseList()				
	return my_linked_list.leftElement()

def quickSearchMethod(array,k):
	return KthSmallest(array,0,len(array)-1,k)

if __name__ == "__main__":
	array = [3,52,66,64,28,9,44,70,72,1,0]
	for i in range(10):
		k = int(input())
		print(linkedListMethod(array,k))
		print(quickSearchMethod(array,k))	