import Node

def main():

    def printList(aList):
        for item in aList:
            print(item)
        print("\n")

    # Create node instances
    personNode1 = Node.Node("Sally")
    personNode2 = Node.Node("Jerry")
    personNode3 = Node.Node("Bob")
    personNode4 = Node.Node("Mary")

    personList = [personNode1, personNode2,
                  personNode3, personNode4]
    printList(personList)

    # Test Copy
    personCopyList = []
    for person in personList:
        personCopyList.append(person.copyNode())
    printList(personCopyList)

    # Test linking
    personList[0].nextNode = personList[1]
    print(personList[0].getNextNode())

    getNodeInfo(personNode1)


if __name__ == '__main__':
    main()
