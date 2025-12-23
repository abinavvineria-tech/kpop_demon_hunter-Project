import os
# let's create a function that reads a text file and returns the number of lines in it.os


def count_lines_in_file(file_path):
    return sum(1 for line in open(file_path, 'r'))


if __name__ == "__main__":
    file_path = 'sample.txt'
    # Create a sample text file for demonstration
    with open(file_path, 'w') as f:
        f.write("Hello, World!\nThis is a sample file.\nIt has multiple lines.\n")

    line_count = count_lines_in_file(file_path)
    print(f"The file '{file_path}' has {line_count} lines.")

    # Clean up the sample file
    os.remove(file_path)
# let's create a user for huntrix in django
