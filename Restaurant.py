order = []
salesTax = 9.75

def restaurantgreetin():
    print("Boudreaux & Thibodeaux's Restaurant")
    print("------------------------------------")


def menu():
   
        print("Menu")
        print("1.Croissant: $3.95")
        print("2.King Cake Slice: $4.95")
        print("3.Crawfish Pie: (by the slice): $3.65")
        print("4.Catfish Poboy: $14.95")
        print("5.Roastbeef Poboy: $13.95")
        print("6.Sausge poboy: $12.95")
        print("7.Gumbo: $5.95")
        selction = input("What would you like to order? Type the appropriate number of the menu item: ")
        if selction == "1":
            order.append(3.95)
        elif selction == "2":
             order.append(4.95)
        elif selction == "3":
             order.append(3.65)
        elif selction == "4":
             order.append(14.95)
        elif selction == "5":
             order.append(13.95)
        elif selction == "6":
             order.append(12.95)
        elif selction == "7":
             order.append(5.95)
             
              subtotal = sum(order)
    total_order = subtotal + (subtotal * salesTax)
    return total_order

  



restaurantgreetin()
menu()
print("Your total including tax is: ${:.2f}".format(total))

