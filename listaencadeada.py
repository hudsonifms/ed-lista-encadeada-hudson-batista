class node:
    def __init__(self, data=None):
        self.data = data
        self.ponteiro = None
                
class encadeamento:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __getitem__(self, index):
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
        if self.head is None:
            self.head = node(value)
            self.size += 1
            return
        
        node_iterado = self.head

        while node_iterado.ponteiro != None:
            node_iterado = node_iterado.ponteiro
            
        novo_node = node(value)
        node_iterado.ponteiro = novo_node
        self.size += 1
        
# remove(value) — remover um elemento da lista
    def remove(self, index):
        if self.size <= index:
            raise IndexError("index não existe")
        
        if index == 0:
            self.head = self.head.ponteiro
            self.size -= 1
            return
        
        node_iterado = self.head
        for i in range(index-1):
            node_iterado = node_iterado.ponteiro           
        node_iterado.ponteiro = node_iterado.ponteiro.ponteiro
        self.size -= 1
         
# search(value) — buscar um elemento na lista
    def search(self, index):
        return self.get(index)

# print_list() — imprimir os elementos da lista
    def show(self):
        node_iterado = self.head
        if node_iterado is None:
            print("[]")
            return
        while node_iterado:
            print(node_iterado.data)
            node_iterado = node_iterado.ponteiro

# size() — retornar o tamanho da lista
        
    def __len__(self):
        return self.size
    
# is_empty() — verificar se a lista está vazia
    def is_empty(self):
        return self.size == 0
            
        

        