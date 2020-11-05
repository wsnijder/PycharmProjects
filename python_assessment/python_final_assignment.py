import pandas as pd
import os

# Starting point question for making a invoice.
startingpoint = int(input("Hello! Press 1 to start invoice."))
if startingpoint != 1:
    exit()
print("Alright, let's go!")
out = open('totalinvoice.txt', 'w')

# Retrieve current invoice number from invoices.csv, return this with +1, and save this in invoices.csv
pd.read_csv("invoices.csv")
df = pd.read_csv("invoices.csv")
dat = df.iloc[[-1]]
invoicenumber = (dat['invoicenumber'].tolist()[0]) + 1
out.write("-------------------------------------------------------" + "\n")
print("The invoicenumber is: " + str(invoicenumber))
out.write("Invoicenumber: " + str(invoicenumber) + "\n")

# Date
from datetime import date
today = date.today()
out.write("Date:" + " " + str(today) + "\n")
out.write("-------------------------------------------------------" + "\n")

# Requesting clientsname. If in clients.csv, address is retrieved. Otherwise manually fill it in, and save in clients.csv.
print("Check our client databese for the clientname of exising clients.")
clientname = input("What is the clientname?")
df_clients = pd.read_csv("clients.csv")
if clientname in df_clients["clientname"].values:
    data_streetnumber = df_clients[df_clients.clientname == clientname]
    streetnumber = (data_streetnumber['street_number'].tolist()[0])
    print("Streetnumber: " + str(streetnumber))
    data_zipcode = df_clients[df_clients.clientname == clientname]
    zipcode = (data_zipcode['zipcode'].tolist()[0])
    print("Zipcode: " + str(zipcode))
    inputquestion = input("Press 1 if correct.")
    if inputquestion != "1":
        streetnumber = input("What is clients streetname plus housenumber?")
        zipcode = input("What is clients zipcode?")
        print("Client has been added to clients.csv")
else:
    streetnumber = input("What is clients streetname plus housenumber?")
    zipcode = input("What is clients zipcode?")
    print("Client has been added to clients.csv")
    # Saving data for new client in clients.csv
    from csv import writer
    def append_list_as_roww(file_namee, list_of_elemm):
        with open(file_namee, 'a+', newline='') as write_objj:
            csv_writer = writer(write_objj)
            csv_writer.writerow(list_of_elemm)
    row_contentss = [clientname, streetnumber, zipcode]
    append_list_as_roww('clients.csv', row_contentss)
out.write("Name: " + str(clientname) + "\n")
out.write("Streetname & housenumber: " + str(streetnumber) + "\n")
out.write("Zipcode: " + str(zipcode) + "\n")
out.write("-------------------------------------------------------" + "\n")

# Quantity of the products that are ordered, and calculation of total price.
howmanyorder = int(input("How many total orders?"))
totaltotal = []
print("Check our list of products in products.csv")
for x in range(howmanyorder):
    productnumber = input("What is the productnumber?")
    df_products = pd.read_csv("products.csv")
    if int(productnumber) in df_products["productnumber"].values:
        data_products = df_products[df_products.productnumber == int(productnumber)]
        price = data_products['price'].tolist()[0]
        data_description = df_products[df_products.productnumber == int(productnumber)]
        description = data_description['description'].tolist()[0]
    quantity = int(input("What is the quantity?"))
    total = int(price) * quantity
    totaltotal.append(total)
    out.write("Product: " + str(description) + "\n")
    out.write("Price: " + str(price) + "\n")
    out.write("Quantity: " + str(quantity) + "\n")
    out.write("Total price: " + str(total) + "\n")
    out.write("-------" + "\n")

# Calculating total price
tot = sum(totaltotal)
out.write("Total price: " + str(tot) + " euro" + "\n")

# Calculating the total price with VAT.
vatrate = int(input("What is the VAT percentage for this order?"))
out.write("VAT %: " + str(vatrate) + "\n")
totalwithvat = tot * (1 + (vatrate/100))
formatted_totalwithvat = "{:.2f}".format(totalwithvat)
out.write("Total price with VAT: " + str(formatted_totalwithvat) + " euro" + "\n")
out.write("-------------------------------------------------------" + "\n")

# closing en reopening invoice in totalinvoice.txt
out.close()

verification = input("Press 1 if this information is right.")
if verification != '1':
    print("Unfortunately, try again!")
    exit()
else: print("Done! Invoice has been added to invoices.csv")

# Saving invoice information in invoices.csv
from csv import writer
def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
row_contents = [invoicenumber, clientname, description, price, quantity, tot, vatrate, totalwithvat]
append_list_as_row('invoices.csv', row_contents)