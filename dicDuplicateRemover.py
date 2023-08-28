import sys
import re

def is_valid_hex_string(s):
    return re.match(r'^[0-9A-F]{12}$', s) is not None

def remove_invalid_strings(input_file_path):
    removed_strings = []  # To store removed strings and their line numbers

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    valid_lines = []

    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        words = line.split()

        is_line_valid = True
        for word in words:
            if len(word) == 12 and is_valid_hex_string(word):
                continue
            else:
                is_line_valid = False
                removed_strings.append((word, line_num))  # Log removed strings
                break
        
        if is_line_valid:
            valid_lines.append(line)

    with open(input_file_path, 'w') as file:
        file.writelines('\n'.join(valid_lines))

    if removed_strings:
        print("Invalid strings removed:")
        for removed_string, line_num in removed_strings:
            print(f"String '{removed_string}' removed from line {line_num}")
    else:
        print("No invalid strings found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dicDuplicateRemover.py input_file")
        sys.exit(1)

    input_file_path = sys.argv[1]
    remove_invalid_strings(input_file_path)
