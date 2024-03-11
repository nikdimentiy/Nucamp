class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        """Return the size of the queue."""
        return len(self.items)

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first item in the queue."""
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        """Display all items in the queue."""
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        """Take an ice cream order from a customer."""
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor!")
            return
        if scoops == 0 or scoops > 3:
            print("Please choose between 1-3 scoops!")
            return

        print("Order Created!")

        order = {"customer": customer, "flavor": flavor, "scoops": scoops}

        self.orders.enqueue(order)

    def show_all_orders(self):
        """Display all pending ice cream orders."""
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders.items:
            print("Customer:", order["customer"], "--Flavor:",
                  order["flavor"], "--Scoops:", order["scoops"])

    def next_order(self):
        """Process the next ice cream order."""
        next_order = self.orders.dequeue()
        if next_order:
            print("\nNext Order Up!")
            print("Customer:", next_order["customer"], "--Flavor:",
                  next_order["flavor"], "--Scoops:", next_order["scoops"])
        else:
            print("\nNo pending orders!")


# Test the IceCreamShop class
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)  # Invalid order
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()  # Bruce's invalid order should be removed
