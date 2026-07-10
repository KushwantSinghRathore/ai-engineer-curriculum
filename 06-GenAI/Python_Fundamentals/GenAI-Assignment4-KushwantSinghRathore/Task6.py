import os

file_name = input("Enter the accurate file name to open: ")
if os.path.exists(file_name):
    with open(file_name,"r") as f:
        print(f.read())
else:
    print("File not found. Please check filename.")        