# Read the file VendorList.csv into this program and create a dictionary of the customer's
# full name, email address and phone number where the key is the full name of the customer
# and the value is a dictionary where the keys are 'email' and 'phone' and the values
# are the corresponding email address and phone number of the customer. 

# Once the dictionary has been completed print it out. It shoud resemble what is shown
# below (first 2 and last 2 elements shown only):

#{'Tommie Goody': {'email': 'tgoody0@weather.com', 'phone': '809-992-7298'}, 
# 'Obadiah Godfery': {'email': 'ogodfery1@a8.net', 'phone': '560-745-9361'}......
# ..........'Kessiah Tynemouth': {'email': 'ktynemouthdu@ning.com', 'phone': '690-215-8097'}, 
# 'Carmela Kaubisch': {'email': 'ckaubischdv@wikia.com', 'phone': '307-726-6526'}}


# Using the dictionary, write the contents to a csv file. The output file shoud be exactly as
# what is shown in the file - marketinglist.csv.
# Name your file - marketinglistFINAL.csv


# Note: you can use the comments below to guide you through the logic of the code. You are not
# required to follow it. ALSO NOT ALL STEPS HAVE BEEN COMMENTED. You may have additional steps.


import csv

# open the vendorlist file
vendor_list = open('VendorList.csv', 'r')

# create a csv object from the file object
csv_file = csv.reader(vendor_list)

# create an output file
marketing_list = open('marketinglistFINAL.csv', 'w')

next(csv_file)


# create an empty dictionary
new_dictionary = {}


# iterate through the csv object
for record in csv_file:
    new_dictionary [record[4]] = (f'phone: {record[5]}')

#(f'phone: {record[5]}')

    # add the key-value pair to the dictionary



# print the dictionary after the loop is finished
print(new_dictionary)


# iterate through the dictionary and write to the output file
for record in new_dictionary:
    marketing_list.write(record)



# close your output file
marketing_list.close()
