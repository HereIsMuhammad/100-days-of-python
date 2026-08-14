# Day 64: CSV File Handling

import csv

# Writing CSV File
def write_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["Name", "Age", "Marks"])

        # Data
        writer.writerow(["Ali", 20, 85])
        writer.writerow(["Ahmad", 21, 90])
        writer.writerow(["Sara", 19, 88])

    print("CSV file written successfully!")


# Reading CSV File
def read_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            print("\nCSV Data:")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("File not found. Please write data first.")


# Run
write_csv()
read_csv()