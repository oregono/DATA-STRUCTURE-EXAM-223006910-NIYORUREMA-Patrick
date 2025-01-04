class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot add more tickets.")
            return
        if self.front == -1:  
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Added: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! No tickets to process.")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:  
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Processed: {data}")
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue contents:", end=" ")
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print()


queue = CircularQueue(5)

queue.enqueue("Ticket 1")
queue.enqueue("Ticket 2")
queue.enqueue("Ticket 3")
queue.display()

queue.dequeue()
queue.display()

queue.enqueue("Ticket 4")
queue.enqueue("Ticket 5")
queue.enqueue("Ticket 6")  
queue.display()
