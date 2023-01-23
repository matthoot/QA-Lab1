import csv

while(True):
    print("Enter your name: ")
    name = input()
    validID = False
    while (not validID):
        print("Enter your 9 digit TUID: ")
        tuID = input()
        if tuID.isnumeric():
            if len(tuID) == 9:
                validID = True
    print("Enter your email address: ")
    email = input()
    print("Enter your phone number ")
    phone = input()
    print("Enter your major: ")
    major = input()
    print("Enter your expected graduation date: ")
    graduation = input()
    print("are you an undergraduate student? (Y/N) ")
    undergraduate = input()

    with open("output.csv", "a") as output_file:
        writer = csv.writer(output_file)
        writer.writerow([name, tuID, email, phone, major, graduation, undergraduate])
    print("Would you like to input another student? (Y/N)")
    another = input()
    if another == "N":
        quit()
