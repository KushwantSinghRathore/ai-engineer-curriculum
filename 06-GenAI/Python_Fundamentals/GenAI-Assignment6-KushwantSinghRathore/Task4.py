filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        # Read the first 3 lines
        for i in range(3):
            line = file.readline()
            if line:
                print(f"Line {i+1}: {line.strip()}")
            else:
                break # Stop if the file has fewer than 3 lines

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    # A catch-all for any other unexpected errors
    print(f"An unexpected error occurred: {e}")

finally:
    print("File operation attempted.")