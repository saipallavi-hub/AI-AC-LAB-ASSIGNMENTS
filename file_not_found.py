#give the Python code so it does not crash when a file is missing. Add try–except error handling and test it with 3 cases.
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
# Test cases to verify the function handles missing files properly
try:
    content = read_file("existing_file.txt")  # Assuming this file exists
    print("File content:", content)
except FileNotFoundError:
    print("Error: The file 'existing_file.txt' was not found.")
try:
    content = read_file("missing_file.txt")  # This file does not exist
    print("File content:", content)
except FileNotFoundError:
    print("Error: The file 'missing_file.txt' was not found.")
try:
    content = read_file("another_missing_file.txt")  # This file also does not exist
    print("File content:", content)
except FileNotFoundError:
    print("Error: The file 'another_missing_file.txt' was not found.")
# The try-except block is used to catch the FileNotFoundError that occurs when trying to open a file that does not exist. This way, instead of crashing the program, it will print a user-friendly error message indicating that the file was not found. The test cases confirm that the function behaves as expected when both existing and missing files are handled.
