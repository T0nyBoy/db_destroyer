from faker import Faker
import csv
import random

fake = Faker()

emails = []
passwords = []
names = []
surnames = []
companies = []


domains = ["org", "com", "net", "edu", "co.uk", "co"]

while True:
    emailPassNr = input("How many emails you need to create? ")
    if emailPassNr.isdigit():
        emailPassNr = int(emailPassNr)
        break
    else:
        print("Invalid input. Please enter a valid integer.")

for i in range(emailPassNr): 
    password = fake.password()
    company = fake.company().replace(" ", "").replace(",", "-").lower()
    domain = random.choice(domains)

    name = fake.name()
    name_parts = name.split()
    first_name = name_parts[0]
    surname = name_parts[-1]

    email = f"{first_name}.{surname}@{company}.{domain}".lower()
    emails.append(email)
    passwords.append(password)
    names.append(first_name)
    surnames.append(surname) 

with open("payload.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name","Surname", "Email", "Password"])
    writer.writerows(zip(names,surnames,emails, passwords))