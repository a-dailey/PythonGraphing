
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 2
        self.back = 2
        self.num_items = 0

        #'''Creates an empty Queue with a capacity'''
    def is_empty(self):
        return self.num_items == 0 and self.capacity != 0
        # '''Returns True if the Queue is empty, and False otherwise
        #    MUST have O(1) performance'''
    def is_full(self):
        return self.num_items == self.capacity
        # '''Returns True if the Queue is full, and False otherwise
        #    MUST have O(1) performance'''
    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        else:
            self.items[self.back] = item
            self.num_items += 1
            self.back += 1
            if self.back == self.capacity:
                self.back = 0
        # '''If Queue is not full, enqueues (adds) item to Queue
        #    If Queue is full when enqueue is attempted, raises IndexError
        #    MUST have O(1) performance'''
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        else:
            front = self.items[self.front]
            self.front += 1
            self.num_items -= 1
            if self.front == self.capacity:
                self.front = 0
            return front
        # '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
        #    If Queue is empty when dequeue is attempted, raises IndexError
        #    MUST have O(1) performance'''
    def size(self):
        return self.num_items
        # '''Returns the number of elements currently in the Queue, not the capacity
        #    MUST have O(1) performance'''


