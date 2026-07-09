sales = [1200, 450, 980, 1500, 3000]

#writng to the file
with open("sales_data.txt", "w") as f:
    for x in sales:
        f.write(str(x) +"\n")

print("Contents of sales_data.txt:")
with open("sales_data.txt", "r") as file:
    #Read and print the lines
    print(file.read())

with open("sales_data_comma.txt", "w") as f:
    for x in sales:
        f.write(str(x) +", ")

print("Contents of sales_data.txt:")
with open("sales_data_comma.txt", "r") as file:
    #Read and print the comma seprated data
    print(file.read())