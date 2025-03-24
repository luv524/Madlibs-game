# menu of these itmes customer wants to buy
menu ={
'pizza':  40,
'burger': 55,
'maggie': 78,
'coffee': 30
}
#  greeting for the customer
print("welcome the cafe bitch")
#menu display
print("pizza: rs40\nburger: rs55\nmaggie: rs 78\ncoffee:30\n")

#toatl of how many things customer ordered
order_total = 0

#first item 
item1 = input("enter item you want to order: ")
if item1 in menu:
    order_total += menu[item1]
    print(f"your item {item1} has been added to your order. ") 
else:
    print(f"order item{item1} is not avliable. ")
    
# asking if customer wants to add another item
another_order = input("do you want to add another item ? (yes / no): ")
if another_order == "yes":
    item2 = input("enter item you want to order: ")
# adding item 2 in this than
if item2 in menu:
    order_total += menu[item2] 
    print(f"item {item2}has been added to the order. ")
else:
    print(f"the item{item2} is not present in the resturant bitch. ")

#the total sum would be this after all the added items
print(f"the total amount of your orderd items is: Rs {order_total} ")
