#linked list
class Node:
    def __init__(self, data = None):
        self.data = data;
        self.next = None

class linkList:
    def __init__(self):
        self.headval = None;
        
    def printLinkList(self):
        printvalue = self.headval
        while printvalue is not None:
            print(printvalue.data , "->", end = "");
            printvalue = printvalue.next;
############################### link list insertion ######################################
            
    def insertBegining(self,newdata):
        newNode = Node(newdata);
        newNode.next = self.headval;
        self.headval = newNode;
        
    def insertEnd(self, newdata):
        newNode = Node(newdata);
        if self.headval is None:
            self.headval = newNode
            return
        lastnode = self.headval
        while(lastnode.next):
            lastnode = lastnode.next;
        lastnode.next = newNode;
        
    def insertInBetween(self,middleNode,newdata):
        if middleNode is None:
            print("node is absent");
            return
        newNode = Node(newdata);
        newNode.next = middleNode.next
        middleNode.next = newNode
####################################### link list deletion######################################
    def removeNode(self, removekey):
        hvalue = self.headval
        if(hvalue is not None):
            if(hvalue.data == removekey):
                self.headval = hvalue.next;
                hvalue = None
                return
        while(hvalue is not None):
            if(hvalue.data == removekey):
                break;
            prev = hvalue;
            hvalue = hvalue.next
        if(hvalue == None):
            return
        prev.next = hvalue.next;
        hvalue = None

            
        
        

######################## connecting nodes via link #####################
'''ll1 = linkList();
ll1.headval = Node(91)
N2 = Node(90)
#N3 = Node(89)
ll1.headval.next = N2
#N2.next = N3
#print(N2.data);
ll1.insertInBetween(N2.next,87);
ll1.printLinkList();'''



#print(N3.data);'''
l1 = linkList();
l1.headval = Node(10);
n2 = Node(20);
n3 = Node(30);
n4 = Node(40);
l1.headval.next = n2;
n2.next = n3;
n3.next = n4;
l1.printLinkList();
print("\n");
l1.insertBegining(67);
l1.printLinkList();
print("\n");
l1.insertEnd(99)
l1.printLinkList();
print("\n")
l1.insertInBetween(n2.next,87);
l1.printLinkList();
print("\n");
l1.removeNode(67);
l1.printLinkList();

#################automated link list ##################################

n= int(input("\nenter the size"));
obj = linkList();
for i in range(n):
       x = input();
       obj.insertEnd(x);
obj.printLinkList();
       

       




        






