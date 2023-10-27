class sport_mart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}
    def createorder(self, orderid ,itemname ,quantity ,price,total): 
        temp = {
            "orderid": orderid,
            "itemid": itemname,
            "quantity": quantity,
            "price": price,
            "total":total
        }  
        self.orders[orderid] = temp
    def createinventoryitem(self,productid ,productname ,quantity,price):
        temp = {
            "productid": productid,
            "productfile": productname,
            "quantity": quantity,
            "price": price
        }
        self.inventory[productid] = temp
    def printorders(self):
        print(self.orders)
    def printinventory(self):
        print(self.inventory)
trinity = sport_mart()
orders = open("Copy of ORDER.csv","r")
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(",")
    trinity.createorder (temp[0],temp[1],temp[2],temp[3],temp[4])
trinity.printorders()


#creat a menue driven program that will 
#creat new order and update the inventory accordingly 
#export the final data to file
def display_menu():
    print("\nMenu:")
    print("1. Create New Order")
    print("2. Update Inventory")
    print("3. Export Order Data to File")
    print("4. Exit")

trinity = sport_mart()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        orderid = input("Enter Order ID: ")
        itemname = input("Enter Item Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        total = quantity * price
        trinity.createorder(orderid, itemname, quantity, price, total)
    elif choice == '2':
        productid = input("Enter Product ID: ")
        productname = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        trinity.createinventoryitem(productid, productname, quantity, price)
    elif choice == '3':
        with open("order_summary.txt", "w") as file:
            file.write("Order Summary:\n")
            for orderid, order in trinity.orders.items():
                file.write(f"Order ID: {orderid}, Item: {order['itemid']}, Quantity: {order['quantity']}, Price: {order['price']}, Total: {order['total']}\n")
            file.write("\nInventory:\n")
            for productid, product in trinity.inventory.items():
                file.write(f"Product ID: {productid}, Product Name: {product['productfile']}, Quantity: {product['quantity']}, Price: {product['price']}\n")
        print("Data exported to 'order_summary.txt'.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
