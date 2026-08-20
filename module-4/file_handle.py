filename = "comming-soon.txt"

try:
    with open(filename, "r") as file:
        for line in file:
            print(line) 
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print("Enble premission to read or write.") # use this cmd to change 'chmod a-r comming-soon.txt' 
except FileExistsError:
    print("File Exists Error")