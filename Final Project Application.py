from abc import ABCMeta, abstractmethod

class Person:
    def __init__(self, gender, first_name, last_name, address):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        
    def get_gender(self):
        return self.gender
        
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_address(self):
        return self.address
    
class Customer(Person):
    def __init__(self, gender, first_name, last_name, address):
        super().__init__(gender, first_name, last_name, address)
        self.__id_number = NewCustomerID()
        self.__rewards_points = 0
        
    def get_id_number(self):
        return self.__id_number
    
    def get_reward_points(self):
        return self.__rewards_points
    
    def add_rewards_points(self, item_points):
        self.__rewards_points = self.__rewards_points + item_points
        
class NewCustomerID():
    __instance = None
    
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = 1
        else:
            cls.__instance += 1
        return cls.__instance
    
class MenuItem(metaclass=ABCMeta):
    def __init__(self, price, description, rewards_points):
        self.price = price
        self.description = description
        self.rewards_points = rewards_points
        
    @abstractmethod
    def get_name(self):
        pass
        
    def __str__(self):
        return "{} - {} (${:.2f})".format(self.get_name(), self.description, self.price)
    
    def get_rewards_points(self):
        return self.rewards_points
    
class CheesePizza(MenuItem):
    def get_name(self):
        return "Cheese Pizza"
    
class PepperoniPizza(MenuItem):
    def get_name(self):
        return "Pepperoni Pizza"
    
class SausagePizza(MenuItem):
    def get_name(self):
        return "Sasuage Pizza"
    
class MenuFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        
        if name == "cheese pizza":
            return CheesePizza(*args)
        elif name == "pepperoni pizza":
            return PepperoniPizza(*args)
        elif name == "sausage pizza":
            return SausagePizza(*args)
        
class Order():
    def __init__(self):
        self.order_list = []
        self.item_prices = []
        self.item_rewards = []
        self.order_id_number = NewOrderID()
        
    def add_order_list(self, item):
        self.order_list.append(item)
        
    def remove_order_list(self, item_pos):
        self.order_list.pop(item_pos)
        
    def add_item_price(self, price):
        self.item_prices.append(price)
        
    def remove_item_price(self, price_pos):
        self.item_prices.pop(price_pos)
        
    def add_item_reward(self, reward):
        self.item_rewards.append(reward)
        
    def remove_item_reward(self, reward_pos):
        self.item_rewards.pop(reward_pos)
        
    def print_order_contents(self):
        for item in self.order_list:
            print(item)
            
    def order_price_total(self):
        return sum(self.item_prices)
        
    def order_rewards_total(self):
        return sum(self.item_rewards)
            
class NewOrderID():
    __instance = None
    
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = 1
        else:
            cls.__instance += 1
        return cls.__instance

def customer_options():
    print("Enter (1) to view ABC Pizza's menu.")
    print("Enter (2) to add a cheese pizza to your order.")
    print("Enter (3) to add a pepperoni pizza to your order.")
    print("Enter (4) to add a sausage pizza to your order.")
    print("Enter (5) to remove an item from your order.")
    print("Enter (6) to go to the order confirmation screen.")
    print("Enter (7) to cancel your order and exit the application.")
    choice = input("Enter your choice here: ")
    return choice

def view_menu():
    print("")
    menu_item_1 = MenuFactory().create("cheese pizza", 14.00, "Medium-sized pizza with cheese and tomato sauce", 5)
    print(menu_item_1)
    menu_item_2 = MenuFactory().create("pepperoni pizza", 15.50, "Medium-sized pizza with cheese, pepperoni, and tomato sauce", 5)
    print(menu_item_2)
    menu_item_3 = MenuFactory().create("sausage pizza", 15.50, "Medium-sized pizza with cheese, sausage, and tomato sauce", 10)
    print(menu_item_3)
    print("")
    return menu_item_1, menu_item_2, menu_item_3

def add_to_order(order, item):
    order.add_order_list("{} (${:.2f})".format(item.get_name(), item.price))
    order.add_item_price(item.price)
    order.add_item_reward(item.rewards_points)
    print("")
    print("1x {} added to your order.".format(item.get_name()))
    print("")
    

def create_order():
    test_customer = Customer("Male", "Bill", "Oden", "652 Gold Lane, New York, NY, 05278")
    print("Welcome to ABC Pizza, {}. What will you be having today?".format(test_customer.get_first_name()))
    menu_item_1, menu_item_2, menu_item_3 = view_menu()
    choice = customer_options()
    new_order = Order()
    while True:
        if not(choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7"):
            print("ERROR: Invald input")
            choice = input("Enter your choice here: ")
        elif choice == "1":
            menu_item_1, menu_item_2, menu_item_3 = view_menu()
            choice = customer_options()
        elif choice == "2":
            add_to_order(new_order, menu_item_1)
            choice = customer_options()
        elif choice == "3":
            add_to_order(new_order, menu_item_2)
            choice = customer_options()
        elif choice == "4":
            add_to_order(new_order, menu_item_3)
            choice = customer_options()
        elif choice == "5":
            while True:
                if new_order.order_list == []:
                    print("")
                    print("ERROR: No items selected for order.")
                    print("")
                    choice = customer_options()
                    break
                else:
                    print("")
                    print("Current Order:")
                    print("")
                    new_order.print_order_contents()
                    print("")
                    removal_selection = input("Enter the numerical number associated with the item you would like to remove, or enter (0) to exit back to the menu. For example, to remove the first item of your order, enter (1): ")
                    while True:
                        try:
                            if removal_selection == "0":
                                print("")
                                choice = customer_options()
                                break
                            else:
                                new_order.remove_order_list(abs(int(removal_selection)) - 1)
                                new_order.remove_item_price(abs(int(removal_selection)) - 1)
                                new_order.remove_item_reward(abs(int(removal_selection)) - 1)
                                print("")
                                print("Item has been removed successfully")
                                print("")
                                choice = customer_options()
                                break
                        except:
                            print("ERROR: Invalid input")
                            removal_selection = input("Enter the numerical number associated with the item you would like to remove, or enter (0) to exit back to the menu. For example, to remove the first item of your order, enter (1): ")
                    break
        elif choice == "6":
            while True:
                if new_order.order_list == []:
                    print("")
                    print("ERROR: No items selected for order.")
                    print("")
                    choice = customer_options()
                    break
                else:
                    print("")
                    print("Order Details:")
                    print("")
                    new_order.print_order_contents()
                    print("------------------------")
                    print("Order Total: ${:.2f}".format(new_order.order_price_total()))
                    print("")
                    order_confirmation = input("Do you want to submit this order? (y/n): ")
                    while True:
                        if not(order_confirmation == "y" or order_confirmation == "n"):
                            print("ERROR: Invald input")
                            order_confirmation = input("Do you want to submit this order? (y/n): ")
                        elif order_confirmation == "y":
                            print("")
                            print("Your order has been submitted and will be delivered shortly. Thank you for choosing ABC Pizza!")
                            print("Rewards points earned: {}".format(new_order.order_rewards_total()))
                            test_customer.add_rewards_points(new_order.order_rewards_total())
                            print("New rewards points balance: {}".format(test_customer.get_reward_points()))
                            exit()
                        elif order_confirmation == "n":
                            print("")
                            choice = customer_options()
                            break
                    break
        elif choice == "7":
            print("")
            exit_confirmation = input("Are you sure you want to cancel this order and exit the application? (y/n): ")
            while True:
                if not(exit_confirmation == "y" or exit_confirmation == "n"):
                    print("ERROR: Invalid input")
                    exit_confirmation = input("Are you sure you want to cancel this order and exit the application? (y/n): ")
                elif exit_confirmation == "y":
                    print("")
                    print("Order has been cancelled. Thank you for using ABC Store's ordering application, and we hope to see you soon!")
                    exit()
                elif exit_confirmation == "n":
                    print("")
                    choice = customer_options()
                    break

def main():
    create_order()
    
main()