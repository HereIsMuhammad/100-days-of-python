# Day 65: JSON File Handling

import json

# Writing JSON File
def write_json():
    data = {
        "username": "Ahmad",
        "theme": "dark",
        "notifications": True,
        "volume": 75
    }

    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)

    print("JSON file written successfully!")


# Reading JSON File
def read_json():
    try:
        with open("config.json", "r") as file:
            data = json.load(file)

            print("\nConfig Data:")
            for key, value in data.items():
                print(f"{key}: {value}")

    except FileNotFoundError:
        print("File not found. Please write data first.")


# Run
write_json()
read_json()