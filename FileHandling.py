
try:
    
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, welcome to file handling.\n")
        file.write("Line 2: Today is a great day to learn Python.\n")
        file.write("Line 3: Python version 3.10 is amazing.\n")
    print("File created and initial lines written successfully.")
    with open("my_file.txt", "r") as file:
        print("\nReading contents of my_file.txt:")
        print(file.read())

    with open("my_file.txt", "a") as file:
        file.write("Line 4: This is an appended line.\n")
        file.write("Line 5: Adding more data for testing purposes.\n")
        file.write("Line 6: Appending the final line to the file.\n")
    print("\nAdditional lines appended successfully.")

    with open("my_file.txt", "r") as file:
        print("\nReading updated contents of my_file.txt:")
        print(file.read())

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You don't have permission to access or modify this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations complete.")
