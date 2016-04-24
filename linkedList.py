'''
---Vinyas Harish---
Simple procedural linked list with various test functions including the following functionality:
    - create, insert, delete nodes
    - determine the length of the list
    - swap nodes
    - delete nodes with an even-numbered value

'''
#Create a linked list
def createList(plist):
    linkedList = None
    #Goes backwards, adding each element to the beginning of the list.
    for index in range(len(plist)-1, -1, -1):
        linkedList = insertValueHead(linkedList, plist[index])
    return linkedList

#Creates an empty linked list.
def emptyList():
  return None

#Inserts a new value at the head of the linked list.
def insertValueHead(linkedList, value):
    #linkedList is the head of the list to be added to
    #value is the data to be stored in the node
    newnode = {}
    newnode["data"] = value
    #set the next pointer of this new node to the head of the list, linkedList.
    #newnode is now the head of the list.
    newnode["next"] = linkedList
    return newnode

#Obtain the nth node in the list.
def nthNode(linkedList, n):
    ptr = linkedList
    count = 0
    if n < 0:
        return None
    while ptr != None and count < n:
        ptr = ptr['next']
        count += 1
    return ptr

#Insert a node into the list.
def insertNode(list, index, value):
  newNode = {'data':value}
  if index == 0:  #First we handle the case of an empty list.
    newNode['next'] = list #The new node becomes the head of the list.
    return newNode
  else:
      spotBefore = nthNode(list, index-1)
      if spotBefore == None: #We print None since the index is invalid.
        return None
      else:
          spotAfter = spotBefore['next']
          spotBefore['next'] = newNode  #Finally this section of code will be used to add a node elsewhere.
          newNode['next'] = spotAfter
          return list

#Get the length of a linked list.
def countPlaceholders(list):
    if list == {}:
        return 0
    ptr = list
    if ptr == None:
        return None
    else:
        count = 1
        ptr = ptr['next']
        while ptr != None:
            count = count+1
            ptr = ptr['next']
        return count

#Delete a certain node in the list.
def deleteNthNode(list, index):
    if index == 0 and list != None:  #To delete the first node.
        return list['next']
    else:
        spotBefore = nthNode(list, index-1)
        if spotBefore == None:  #Your list is empty. So None is returned
            return None
        nodeSelected = spotBefore['next']
        if nodeSelected == None:
            return None #Since the list is out of range.
        #Switch the pointers of the node before the deleted node in order to reconnect elements in our list.
        spotBefore['next'] = nodeSelected['next']
        return list

#Switch the position of nodes in the list.
def switch(list, index):
  count = countPlaceholders(list) #Obtain the length of the list, which will be useful for making switches.
  switchStart = nthNode(list, index)
  switchEnd = nthNode(list, index+1)
  if count == None:   #Empty list case will return None.
    return None
  elif index >= count-1: #If the index exceeds the length of the list, we cannot make a switch since it will be out of range.
    return None
  else:
    if index == 0:
        switchStart['next'] = switchEnd['next']  #Remove the second node from the list, but keep its pointer and the subsequent nodes in place.
        switchEnd['next'] = switchStart     #Reassign the second node so that it's pointer becomes the rest of the list.
        return switchEnd
    else:
        deleteNthNode(list, index+1)   #Delete the node that will be moved forward.
        insertNode(list, index, switchEnd['data']) #Move the node selected in the line above forward.
    return list

#Remove nodes with even-numbered values in it.
def removeEvens(list):
  node = list
  index = 0
  while node != None:
      if node['data'] %2== 0:
        return removeEvens(deleteNthNode(list,index))
      else:
          index = index+1
          node = node['next']
  return list

#Creates a string representation of the values in the linked list.
def listString(linkedList):
  if linkedList == None:
    return "Careful! This index is out of range."

  ptr = linkedList
  str1 = "["
  while ptr != None:
    str1 += str(ptr['data'])
    ptr = ptr['next']
    if ptr != None:
      str1 += ","
  str1 = str1 + "]"
  return str1

#Prints all the values in the linked list.
def printList(linkedList):
    print listString(linkedList)

#Test code to ensure that 'insertNode()' is working correctly.
def testInsert():
    print "Testing the 'insertNode' function...\n"
    myList = createList([1,2,3,4,5,6])
    print "The initial list:"
    printList(myList)
    myList = insertNode(myList,0,0)
    print "\nInserted 0 at the start of list:"
    printList(myList)
    myList = insertNode(myList,7,7)
    print "\nInserted 7 at the end of list:"
    printList(myList)
    myList= insertNode(myList,3,2.2)
    print "\nInserted 2.2 in the 3rd position:"
    printList(myList)
    myList = insertNode(myList,26,12) #Should generate an out of range error.
    print "\nInserted 12 in the 26th position:"
    printList(myList)

#Test code to ensure that 'switch()' is working correctly.
def testSwitch():
    print "Testing the 'switch' function...\n"
    myList = createList([1,2,3,4,5,6])
    print "The initial list:"
    printList(myList)
    myList = switch(myList,0)
    print "\nSwitching the 0th and the 1st element:"
    printList(myList)
    myList = switch(myList,3)
    print "\nSwitching the 3rd and the 4th element:"
    printList(myList)
    myList = switch(myList,5) #Should result in an error.
    print "\nSwitching the 5th and the 6th element:"
    printList(myList)
    myList = switch(myList,29)#Should result in an error.
    print "\nSwitching the 29th and the 30th element:"
    printList(myList)

#Test code to ensure that 'removeEvens()' is working correctly.
def testRemoveEvens():
    print "Testing the 'removeEvens' function...\n"
    myList = createList([1,7,4,15,16,22])
    print "The initial list:"
    printList(myList)
    myList = removeEvens(myList)
    print "With evens removed, list is:"
    printList(myList)
    myList = createList([2,7,4,15,16,3])
    print "\nThe initial list:"
    printList(myList)
    myList = removeEvens(myList)
    print "With evens removed, list is:"
    printList(myList)

#Bringing it all together...
def main():
    linkedList = emptyList()
    print "Testing the 'insertValueHead' function...\n"
    print "Inserting a new node with value 9"
    linkedList = insertValueHead(linkedList,9)
    printList(linkedList)
    print "\nInserting a new node with value 20"
    linkedList = insertValueHead(linkedList,20)
    printList(linkedList)
    print
    testInsert()
    print
    testSwitch()
    print
    testRemoveEvens()

main()
