class node:
    def __init__(self, data=None):
        self.data = data
        self.ponteiro = None
                
class encadeamento:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add(self, data):
        if(self.head == None):
            self.head = node(data)
            self.size += 1
        
        else:
            node_iterado = self.head
            while(node_iterado.ponteiro):
                node_iterado = node_iterado.ponteiro            
            node_iterado.ponteiro = node(data)
            self.size += 1

    def get(self, index):
        node_iterado = self.head
        
        if(self.size <= index):
            raise IndexError("index não existe")
        for i in range(index):
            node_iterado = node_iterado.ponteiro           

        return node_iterado.data
        
    def __setitem__(self, index, element):
        node_iterado = self.head
        
        if(self.size <= index):
            raise IndexError("index não existe")
        
        for i in range(index):
            node_iterado = node_iterado.ponteiro           

        node_iterado.data = element

    def len(self):
        return self.size
    
    def show(self):
        node_iterado = self.head
        print(node_iterado.data)


        while(node_iterado.ponteiro):
            node_iterado = node_iterado.ponteiro
            print(node_iterado.data)
            
        

caideia = encadeamento()
caideia.add(10)
caideia.add(20)
caideia.add(30)
caideia.add(40)
caideia[3] = 14


caideia.show()
print(caideia.len())







        