# Program that performs stock taking for a warehouse

# class Shoe is created with properties: country, code, product, cost, quantity
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # defining get and set methods for cost,quantity,code,product
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    # defining a method that creates a string for the file entry
    def create_file_entry(self):
        output = f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n'
        return output

    # A block of code that returns a string representation of the class.
    def __str__(self):
        output = '{' + f'Country : {self.country}\n'
        output += f'Code : {self.code}\n'
        output += f'Product : {self.product}\n'
        output += f'Cost : {self.cost}\n'
        output += f'Quantity : {self.quantity}\n' + '}'
        return output


# ==========Functions outside the class==============
# Block of code that reads data from the text file and
# creates an object with this data and appends the object to shoes list
def read_shoes_data():
    file = open('inventory.txt', 'r+')
    file_obj = file.readlines()
    shoe_objects = []
    for index, line in enumerate(file_obj):
        if index != 0:
            line = line.strip("\n")
            line_split = line.split(',')
            object1 = Shoe(line_split[0], line_split[1], line_split[2], int(line_split[3]), line_split[4])
            shoe_objects.append(object1)
    file.close()
    return shoe_objects

# Block of code that will allow a user to capture data
# about a shoe and use this data to create a shoe object
# and append this object inside the shoe list.


def capture_shoes(existing_shoe_list):
    country = input("Enter country name: ")
    code = input("Enter code:")
    product = input("Enter product:")
    cost = input("Enter cost:")
    quantity = input("Enter quantity:")
    shoe_obj = Shoe(country, code, product, cost, quantity)
    existing_shoe_list.append(shoe_obj)
    '''
    # opening the file and appending the shoe object to the text file
    file = open('inventory.txt','a+')
    file.write(shoe_obj.create_file_entry())
    file.close()'''
    return existing_shoe_list


# Block of code that will iterate over the shoes list and
# print the details of the shoes returned from the __str__function.

def view_all(shoe_list):
    for index, shoe_object in enumerate(shoe_list):
        print(shoe_object)


# Block of code that will find the shoe object with the lowest quantity,
# which is the shoes that need to be re-stocked. Ask the user if they
# want to add this quantity of shoes and then update it.
# This quantity is updated on the file for this shoe.


def re_stock(shoe_list):
    lowest_quantity = 0
    lowest_quantity_object = None
    for index, shoe_object in enumerate(shoe_list):
        if index == 0 or (int(shoe_object.get_quantity()) < lowest_quantity):
            lowest_quantity = int(shoe_object.get_quantity())
            lowest_quantity_object = shoe_object
    if not lowest_quantity_object is None:
        print(lowest_quantity_object)
        choice = input("Do you want to add the quantity of shoes?(Y/N): ").lower()
        if choice == 'y':
            add_quantity = int(input("Enter the quantity of shoes you want to add: "))
            updated_quantity = lowest_quantity + add_quantity
            lowest_quantity_object.set_quantity(updated_quantity)
            file = open('inventory.txt', 'w+')
            file.write('Country,Code,Product,Cost,Quantity\n')
            for index1, new_shoe in enumerate(shoe_list):
                if new_shoe.get_code() == lowest_quantity_object.get_code():
                    new_shoe.set_quantity(updated_quantity)
                file.write(new_shoe.create_file_entry())
            file.close()
        else:
            print("Nothing to add.")

# Block of code that will search for a shoe from the list
# using the shoe code and return this object so that it will
# print the details of the shoes returned from the __str__function.


def search_shoe(shoe_list):
    shoe_code = input("Enter the shoe code:")
    for index, shoe_object in enumerate(shoe_list):
        if shoe_code == shoe_object.get_code():
            print(shoe_object)

# Block of code that will calculate the total value for each item.
# Using the formula : value = cost * quantity.
# Print this information on the console for all the shoes.


def value_per_item(shoe_list):
    for shoe_object in shoe_list:
        total_value = int(shoe_object.get_quantity()) * int(shoe_object.get_cost())
        print(f'Total Value of product - {shoe_object.get_product()} is {total_value}')

# Block of code that determine the product with the highest quantity and
# print this shoe as being for sale.


def highest_qty(shoe_list):
    highest_quantity = 0
    highest_quantity_object = None
    for index, shoe_object in enumerate(shoe_list):
        if index != 0 and (int(shoe_object.get_quantity()) > highest_quantity):
            highest_quantity = int(shoe_object.get_quantity())
            highest_quantity_object = shoe_object
    print(f'Shoes on SALE!!!!\n Product: {highest_quantity_object.get_product()}')


# ==========Main Menu=============

# The list will be used to store a list of objects of shoes
# calling read_shoes_data function
shoe_list = read_shoes_data()

# Using while loop to handle the user inputs for the menu
while True:
    menu = input('''Select one of the following Options below:
cs - search product by code and print the cost of the shoe
lq - Determine the product with lowest quantity and restock it
hq - Determine the product with highest quantity and print this shoe for sale
tv - Calculate the total value of the stock item
cd - Capture data about a shoe and append this object inside the list
va - View all details of shoes and print
ss - search shoe using the shoe code and print the details of the shoe
q - quit
: ''').lower()

    # Using if/elif/else conditions to check the input choices and print the output
    # Calling functions based on the menu options
    if menu == 'cs':
        code_name = input("Enter the code of the product: ")
        for index, shoe_object in enumerate(shoe_list):
            try:
                if shoe_object.get_code() == code_name:
                    cost_shoe = shoe_object.get_cost()
                    print(f'cost of the shoe - {cost_shoe}')
                    break
                if index == len(shoe_list) - 1:
                    raise Exception("Code does not exist")
            except:
                print("Code does not exist")

    elif menu == 'lq':
        shoe_list = read_shoes_data()
        re_stock(shoe_list)

    elif menu == 'hq':
        highest_qty(shoe_list)

    elif menu == 'tv':
        value_per_item(shoe_list)

    elif menu == 'cd':
        shoe_list = capture_shoes(shoe_list)

    elif menu == 'va':
        view_all(shoe_list)

    elif menu == 'ss':
        search_shoe(shoe_list)

    elif menu == 'q':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
