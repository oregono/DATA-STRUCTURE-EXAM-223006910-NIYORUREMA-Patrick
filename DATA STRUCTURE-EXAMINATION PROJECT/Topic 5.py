class ReservationNode:
    def __init__(self, reservation_id, event_name, customer_name, tickets_reserved):
        self.reservation_id = reservation_id
        self.event_name = event_name
        self.customer_name = customer_name
        self.tickets_reserved = tickets_reserved
        self.left = None
        self.right = None

class ReservationTree:
    def __init__(self):
        self.root = None

    def insert(self, reservation_id, event_name, customer_name, tickets_reserved):
        new_node = ReservationNode(reservation_id, event_name, customer_name, tickets_reserved)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, current_node, new_node):
        if new_node.reservation_id < current_node.reservation_id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_node(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_node(current_node.right, new_node)

    def search(self, reservation_id):
        return self._search_node(self.root, reservation_id)

    def _search_node(self, current_node, reservation_id):
        if current_node is None or current_node.reservation_id == reservation_id:
            return current_node
        elif reservation_id < current_node.reservation_id:
            return self._search_node(current_node.left, reservation_id)
        else:
            return self._search_node(current_node.right, reservation_id)

    def display(self, node):
        if node:
            self.display(node.left)
            print(f"Reservation ID: {node.reservation_id}, Event: {node.event_name}, Customer: {node.customer_name}, Tickets: {node.tickets_reserved}")
            self.display(node.right)
            
reservation_tree = ReservationTree()
reservation_tree.insert(101, "New Groove concert", "Patrick Nelson", 2)
reservation_tree.insert(102, "RNB Show", "Daneil schiffer", 4)
reservation_tree.insert(100, "Night club show", "Allan K", 1)

reservation_tree.display(reservation_tree.root)

reservation = reservation_tree.search(101)
if reservation:
    print(f"\nReservation Found: {reservation.reservation_id}, Event: {reservation.event_name}, Customer: {reservation.customer_name}")
else:
    print("Reservation not found.")
