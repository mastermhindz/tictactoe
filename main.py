import os

if __name__ == '__main__':
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))

    with open('user_data.txt', 'w') as f:
        f.write(f"{first_name},{last_name},{age}\n")

    with open('user_data.txt', 'r') as f:
        for line in f:
            first_name, last_name, age = line.split(',')
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Age: {age}")