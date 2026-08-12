import json

def json_table(json_file_path):

    # 1. Print the table headers with fixed column spacing
    std_table = f"\n{'Name':<12} | {'Age':<5} | {'Marks':<5}\n"
    std_table += "-" * 32  # Separator line
    std_table += "\n"

    try:
        with open(json_file_path, "r") as file:
            students = json.load(file)
        
        # 2. Loop through and print each student's data aligned to the headers
        for student in students:
            name = student["name"]
            age = student["age"]
            marks = student["marks"]
            
            # <12 aligns text to the left with 12 characters of space
            std_table += f"{name:<12} | {age:<5} | {marks:<5}\n"
        return std_table
    
    except FileNotFoundError:
        return f"Error: The file at {json_file_path} was not found."
    except json.JSONDecodeError:
        return "Error: Failed to decode JSON. Check file format."
