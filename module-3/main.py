import modules.basic_var as ci
from pathlib import Path
from modules.json import json_table
from modules.calc import calc
from modules.qroot import calc_square_roots

json_file_path = Path(__file__).parent / "db" / "students.json"

while True:
    try:
        print("\n=== Choose Any Options === \nOption 1: Basic calculation \nOption 2: Square-root \nOption 3: Import basic variable & Get in-build libary examples \nOption 4: To execute json libary \nOption 5: To view libary modules \nOption 0: To exit")
        option = int(input("Enter your operation: "))
        if option == 0:
            break
        elif option == 1:
            print("\n=== 1. Basic Calculator ===")
            num1 = int(input("\nEnter Number 1: "))
            num2 = int(input("Enter Number 2: "))
            result = calc(num1, num2)
            print(result)
        elif option == 2:
            print("\n=== 2. Square Root Calculator ===")
            num1 = int(input("\nEnter Any Number: "))
            srt = calc_square_roots(num1)
            print(srt)
        elif option == 3:
            print("\n=== 3. Import Basic Variable From Another File ===")
            print(f"\nCollege Name: {ci.college_name} \nCourse: {ci.course} \nSem: {ci.sem} \nTodays Date: {ci.date} \nRandom choice: {ci.rnd}")
        elif option == 4:
            print("\n=== 4. Json Libary ===")
            table_txt = json_table(json_file_path)
            print(table_txt)
        elif option == 5:
            print("\n=== 5. libary Modules ===")
            lib_name = input("\nEnter libary name (ex: math, os, tkinter, numpy): ")
            print(dir(lib_name))
        else:
            print(f"\nERROR: option {option} does't exist...")
    except ValueError:
        print(f"Error: Characters not alllowed")
    except Exception as err:
        print(f"Error: {err}")
