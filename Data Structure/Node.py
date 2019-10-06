class Node():
    """
    This is a Node that stores an object and points to another node
    """

    def __init__(self, anObject):
        """
        Creates a node object using variable 'anObject' as information. Next
        node is set to None
        """
        self.nodeInfo = anObject
        self.nextNode = None


    def  copyNode(self):
        """
        Creates a copy of the current node and returns a node object
        """
        return Node(self.nodeInfo)

    def setNextNode(self, aNode):
        """
        Points current node to another node object
        """
        self.nextNode = aNode

    def getNextNode(self):
        """
        Returns next node
        """
        return self.nextNode

    def clearNextNode(self):
        """
        Sets the next node to None
        """
        self.nextNode = None

    def getNodeInfo(self):
        """
        Retrieve the information stored within the node
        :return: anObject value
        """
        return self.nodeInfo

    def __str__(self):
        """
        Returns data stored inside the node
        """
        return self.nodeInfo


def printNode(aNode):
    if(type(aNode) == Node):
        print(Node)