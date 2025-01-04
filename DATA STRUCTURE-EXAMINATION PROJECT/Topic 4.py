class CircularQueueForOrders:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.queue = [None] * capacity
        self.front = self.rear = -1
        
    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue_order(self, order_id):
        if self.is_full():
            print(f"Queue is full! Cannot add Order ID: {order_id}")
            return
        if self.front == -1:  
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = order_id
        print(f"Order {order_id} added successfully!")

    def dequeue_order(self):
        if self.is_empty():
            print("Queue is empty! No orders to process.")
            return None
        order_id = self.queue[self.front]
        if self.front == self.rear: 
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Processed Order ID: {order_id}")
        return order_id

    def display_orders(self):
        if self.is_empty():
            print("Queue is empty! No orders.")
            return
        print("Current Orders in Queue:", end=" ")
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print()

order_queue = CircularQueueForOrders(3)

order_queue.enqueue_order("Order001")
order_queue.enqueue_order("Order002")
order_queue.enqueue_order("Order003")
order_queue.display_orders()

order_queue.enqueue_order("Order004")  
order_queue.dequeue_order()
order_queue.enqueue_order("Order004")
order_queue.display_orders()
