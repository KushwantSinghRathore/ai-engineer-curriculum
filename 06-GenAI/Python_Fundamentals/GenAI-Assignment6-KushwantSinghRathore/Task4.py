# Task 4: File Reader
filename = input("Enter filename: ")

try:
    file = open(filename, 'r')
    lines = file.readlines()
    # Print first 3 lines (or fewer if file is short)
    count = 0
    for line in lines:
        if count < 3:
            print(line.strip())
            count += 1
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File operation attempted.")