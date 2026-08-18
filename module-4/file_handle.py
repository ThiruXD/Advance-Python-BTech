filename = "comming-soon.txt"

try:
    with open(filename, "r") as file:
        for line in file:
            print(line) 
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")