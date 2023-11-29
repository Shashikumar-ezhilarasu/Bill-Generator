print("---------------------------------------------------------------------------------------------------")
print("\t \t \t \t Welcome to Harvest Heaven")
print("---------------------------------------------------------------------------------------------------")
print("\t \t \t------The Purity of nature's Harvest------")
print("\t    > We are more than just a supermarket")
print("\t    > Our mission: to bring the freshest,healthiest,most delicious foods")
#Our mission: to bring the freshest, healthiest, and most delicious foods
print("\t    > Can't make it to the store? No problem! Explore our online shopping options")
#print("---------------------------------------------------------------------------------------------------")
print("\t Working hours*:10am-11pm  \t \t \t \t \t *Locations:Chennai,Mumbai")
#print("---------------------------------------------------------------------------------------------------")
print("Please Enter the customer details Below")

import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Bala@1207",database="Harvest_heaven")
cur=con.cursor()
transx_id=int(input("Enter transaction id:"))
cust_name=input("Enter customer name:")

Mobile_number=input("Enter Mobile number:")
address=input("Enter customer Address:")
print("Data Added successfully!!,Now You can View it in the mySQL database")
s="insert into customer values('{}','{}','{}','{}')".format(transx_id, cust_name,Mobile_number, address)
cur.execute(s)
con.commit()


print("---------------------------------------------------------------------------------------------------")

def calculate_total(quantity, net_rate):
    return quantity * net_rate

# Initialize total bill
total_bill = 0

# Initialize a list to store entries
entries = []

# Print table header
print("{:<10} {:<15} {:<20} {:<10} {:<10} {:<10}".format("Serial No", "Product ID", "Product Name", "Quantity", "Net Rate", "Total"))

serial_no = 1  # Initial serial number

while True:
    product_id = input("Enter Product ID (or -1 to stop): ")

    # Check if the user wants to stop
    if product_id == "-1":
        break

    product_name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    net_rate = float(input("Enter Net Rate:"))

    # Calculate total
    total = calculate_total(quantity, net_rate)

    # Add total to the overall bill
    total_bill += total

    # Add entry to the list
    entries.append([serial_no, product_id, product_name, quantity, net_rate, total])

    # Increment serial number for the next entry
    serial_no += 1

# Ask the user whether to print the bill
print_bill = input("Do you want to print the bill? (yes/no): ").lower()
print("{:<10} {:<15} {:<20} {:<10} {:<10} {:<10}".format("Serial No", "Product ID", "Product Name", "Quantity", "Net Rate", "Total"))
if print_bill == "yes":
    # Print the data in tabular format
    for entry in entries:
        
        print("{:<10} {:<15} {:<20} {:<10} {:<10} {:<10}".format(*entry))

    # Print the total bill
    print("\nTotal Bill: {:.2f}".format(total_bill))
else:
    print("Bill not printed.")

