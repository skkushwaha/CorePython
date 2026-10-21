"""
Python File Handling Examples
Demonstrates reading, writing, appending, and safe file management.
"""

import os


# 1. Writing to a file (Overwrites existing content)
def write_to_file(filename, content):
    # 'w' mode opens the file for writing and creates it if it doesn't exist
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Successfully written to {filename}")


# 2. Reading an entire file into memory
def read_entire_file(filename):
    try:
        # 'r' mode is the default, used for reading
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."


# 3. Reading a file line by line (Efficient for large files)
def read_file_by_lines(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        print(f"\n--- Reading {filename} line by line ---")
        for line_number, line in enumerate(file, 1):
            # .strip() removes the trailing newline character (\n)
            print(f"Line {line_number}: {line.strip()}")


# 4. Appending data to an existing file
def append_to_file(filename, additional_content):
    # 'a' mode opens the file for appending without erasing previous data
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(additional_content)
    print(f"Successfully appended content to {filename}")


# 5. Safely deleting a file
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' does not exist, cannot delete.")


# --- Execution Workflow ---
if __name__ == "__main__":
    sample_file = "demo_notes.txt"

    # Write initial data
    initial_text = "Line 1: Welcome to Python file handling.\nLine 2: Git tracks this logic.\n"
    write_to_file(sample_file, initial_text)

    # Read the full file
    full_content = read_entire_file(sample_file)
    print("\n--- Full Content Read ---")
    print(full_content)

    # Append fresh lines
    append_to_file(sample_file, "Line 3: Adding a third line asynchronously.\n")

    # Stream data line by line
    read_file_by_lines(sample_file)

    # Clean up (Optional - uncomment to delete the file after run)
    # delete_file(sample_file)
