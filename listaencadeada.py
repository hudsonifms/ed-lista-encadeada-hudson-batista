from tomlkit import value


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
        


# insert_beginning(value) — inserir elemento no início da lista
    def insert_beginning(self, value):
        novo_node = node(value)
        novo_node.ponteiro = self.head
        self.head = novo_node
        self.size += 1

# insert_end(value) — inserir elemento no final da lista
    def insert_end(self, value):
        node = self.ponteiro
        while(node.ponteiro != None):
            node = node.ponteiro
            
        novo_node = node(value)
        node.ponteiro = novo_node
        
# remove(value) — remover um elemento da lista
    def remove(self, index):
        node_iterado = self.ponteiro
        if(self.size <= index):
            raise IndexError("index não existe")
        
        for i in range(index-1):
            node_iterado = node_iterado.ponteiro           
        node_iterado.ponteiro = node_iterado.ponteiro.ponteiro
        self.size -= 1
        
            
# search(value) — buscar um elemento na lista
    def search(self, index):
        node_iterado = self.ponteiro
        if(self.size <= index):
            raise IndexError("index não existe")
        
        for i in range(index):
            node_iterado = node_iterado.ponteiro           
        return node_iterado.data

# print_list() — imprimir os elementos da lista
    def show(self):
        node_iterado = self.head
        print(node_iterado.data)
        
        while(node_iterado.ponteiro):
            node_iterado = node_iterado.ponteiro
            print(node_iterado.data)

# size() — retornar o tamanho da lista
        
    def len(self):
        return self.size
    
            

# is_empty() — verificar se a lista está vazia
    def is_empty(self):
        return self.size == 0
            
        

caideia = encadeamento()
caideia.add(10)
caideia.add(20)
caideia.add(30)
caideia.add(40)
caideia[3] = 14


caideia.show()
print(caideia.len())

        