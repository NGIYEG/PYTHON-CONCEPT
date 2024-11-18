d
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line with a number: 42.\n")
        file.write("Here's the third line, mixing strings and numbers: Python 3.\n")
    print("File created and initial lines written successfully.")

    with open("my_file.txt", "r") as file:
        print("\nReading contents of my_file.txt:")
        print(file.read())

    with open("my_file.txt", "a") as file:
        file.write("This is an appended fourth line.\n")
        file.write("Here's an appended fifth line with a number: 100.\n")
        file.write("Appending a final sixth line to demonstrate append mode.\n")
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
