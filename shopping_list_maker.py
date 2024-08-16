# Task 2
import math

print("Lets create a shopping list!")
start = input("What would you like to add to your shopping list?")

my_list = []
my_list.append(start)


def add_item():
    list_item = input("What would you like to add?")
    my_list.append(list_item)
    return list

def remove_item():
    list_item = input("What item do you want to remove?")
    if list_item not in my_list:
        print("Sorry I don't see that on your list!")
    else:
        my_list.remove(list_item)
        print("Item has been removed")
    return my_list

def show_list():
    i = 1
    for item in my_list:
        print(i,".", item)
        i += 1
    return my_list


session_terminate = False

while session_terminate == False:
    x = input("Would you like to add, remove, view, or exit?")
    if x == "add":
        add_item()
    elif x == "remove":
        remove_item()
    elif x == "view":
        show_list()
    elif x == "exit":
        session_terminate = True
        quit()
    else:
        input("Sorry I don't understand. Would you like to add, remove, view or exit?")