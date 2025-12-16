class ArraySequence:
    """
    A fixed-length array is the data structure that is
    the underlying foundation of our model of com-putation model
     
    (you can think of your computer's memory as a big fixed-length 
    array that your operating system allocates from).
     
    Implementing a sequence using an array, 
    where index i in the array corresponds to item i in the sequence allows 
    get_at  and set_at  to be O(1) time because of our random access machine.  
    
    However, when deleting or inserting into the sequence, 
    we need to move items and resize the array, 
    meaning these operations could take linear-time in the worst case. 
     
    """
    
    def __init__(self):       # O(1)                                                                    
        self.array_sequence = []
        self.size = 0
        
    def __len__(self): return self.size                      # O(1)
    def __iter__(self): yield from self.array_sequence       # O(n) iter_seq
    
    def build(self, *args):                                  # O(n)
        self.array_sequence = [item for item in args] # pretend this builds a static array
        self.size = len(self.array_sequence)
        
    def get_at(self, index:int): return self.array_sequence[index]               # O(1)
    def set_at(self, index:int, new_item):  self.array_sequence[index]=new_item  # O(1)
    
    def _copy_forward(self,                                           # O(N)-N is number of elements to copy
                      start_index, 
                      elements_to_copy, 
                      destination_array, 
                      dest_start_index
        ):   
        for k in range(elements_to_copy): 
            destination_array[dest_start_index + k] = self.A[start_index + k]
            
    def _copy_backward(self, start_index, elements_to_copy, destination_array, dest_start_index):  # O(N)-N is number of elements to copy
        for k in range(elements_to_copy-1, -1, -1): 
            destination_array[dest_start_index + k] = self.A[start_index + k]
            
    def insert_at(self, item_index, item ):  # O(n) n: length of the array
        array_len = len(self)
        new_array = [None] * (array_len + 1)
        self._copy_forward(0, item_index, new_array, 0)
        new_array[item_index] = item 
        self._copy_forward(item_index, array_len-item_index, new_array, item_index+1)
        self.build(new_array)
        
    def delete_at(self, item_index):         # O(n) n: length of the array
        array_len = len(self)
        new_array = [None]*(array_len-1)
        self._copy_forward(0, item_index, new_array, 0)
        deleted_item = self.array_sequence[item_index]
        self._copy_forward(item_index+1, array_len-item_index-1, new_array, item_index)
        return deleted_item
        
        
    def insert_first(self,item): self.insert_at(0,item=item)                            ###### . ######
    def delete_first(self): return self.delete_at(0)                                    #      .      #
    def insert_last(self, new_item): return self.insert_at(len(self), item= new_item)   #     O(n)    #
    def delete_last(self): return self.delete_at(len(self))                             #      .      #
                                                                                        ###### . ######