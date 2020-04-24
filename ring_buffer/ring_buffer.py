from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if buffer is full:
        #     check if current is already at tail, reset
        #     overwrite current
        #     advance current pointer to next node
        # else
        #     add item to tail(append)
        if len(self.storage) == self.capacity:
                #if current pointer is at tail, add new item at head, reset pointer
            if self.current == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                #overwrite current node
                self.storage.insert_node(self.current, item)
                #advance current pointer
                self.current = self.current.next
                self.storage.delete(self.current.next)
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
    
        # TODO: Your code here
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None for i in range(capacity)]
        self.capacity = capacity
        self.current = 0

    def append(self, item):
        if len(self.storage) == self.current:
            self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):
        buffer = [i for i in self.storage if i is not None]
        return buffer
