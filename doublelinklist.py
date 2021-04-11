class Node:
    def __init__(self, data = None):
        self.data = data;
        self.next = None;
        self.prev = None;
class dll:
    def __init__(self):
        self.headval = None;
    
    def printdll(self):
        printvalue = self.headval
        while printvalue is not None:
            print(printvalue.data,"<=>",end="");
            printvalue = printvalue.next;
        #print("End");
    def insertion1(self, newData):
        newNode = Node(newData);
        firstNode = self.headval
        newNode.Next = firstNode.next;
        firstNode.prev = newNode;
        newNode.prev = None;
        


dll1 = dll();
dll1.headval = Node(10);
N2 = Node(20);
N3 = Node(30);
N4 = Node(40);
dll1.headval.next = N2;
N2.prev = dll1.headval;
N2.next = N3;
N3.prev = N2;
N3.next = N4;
N4.prev = N3;
dll1.insertion1(23)
dll1.printdll();
#print(N3.next.data);
        
        
