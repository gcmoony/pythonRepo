import csv
import os


# Initialize variables
ticketList = []
userTicketCount = {}

# Open the file and read the contents
with open(os.path.realpath(__file__).rstrip("equip_checkout.py") + "checkout.csv", newline="") as csvFile:
    reader = csv.reader(csvFile)
    hasTableHeader = True

    for ticket in reader:
        # To skip the table header
        if(hasTableHeader):
            hasTableHeader = False
            continue

        # Add the ticket from the reader to the ticket list
        ticketList.append(ticket)

# Create a set with every username
tempUserList = []
for ticket in ticketList:
    # Get a user name from the ticket
    tempUserList.append(ticket[0].strip())

tempUserList = set(tempUserList)
#print(len(tempUserList))

# Create a dictionary where
    # Key is the username
    # Value initialized to 0
for user in tempUserList:
    userTicketCount[user] = 0

#print(userTicketCount)

for ticket in ticketList:
# Get each tickets username
    # Increase the dict[username] by 1
    userTicketCount[ticket[0]] += 1


# Get radio counts
radioCount = 0
for ticket in ticketList:
    if(ticket[6] == '1'):
        radioCount += 1
print(f'Radio requests: {radioCount}')

# Get laptop counts
laptopCount = 0
for ticket in ticketList:
    if(ticket[2] == '1'):
        laptopCount += 1
print(f'Laptop requests: {laptopCount}')

# Get scanner counts
scannerCount = 0
for ticket in ticketList:
    if(ticket[4] == '1'):
        scannerCount += 1
    if(ticket[7] == '1'):
        scannerCount += 1
print(f'Scanner requests: {scannerCount}')

# Display the dictionary
for user, ticketCount in userTicketCount.items():
    print(f"User \t{user} \t\tsubmitted {ticketCount} tickets within the last week")