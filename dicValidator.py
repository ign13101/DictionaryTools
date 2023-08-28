import sys
import re
from collections import defaultdict

def is_valid_hex_string(s):
    return re.match(r'^[0-9A-F]{12}$', s) is not None

def find_repeated_strings(filepath):
    repeated_strings = defaultdict(list)
    invalid_strings = []

    with open(filepath, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            words = line.split()

            seen_words = set()
            for word in words:
                if len(word) == 12 and is_valid_hex_string(word):
                    if word in seen_words:
                        if word not in repeated_strings:
                            repeated_strings[word] = [[], 0]
                        if line_num not in repeated_strings[word][0]:
                            repeated_strings[word][0].append(line_num)
                            repeated_strings[word][1] += 1
                    else:
                        seen_words.add(word)
                else:
                    invalid_strings.append((word, line_num))

    return repeated_strings, invalid_strings

def main():
    if len(sys.argv) != 2:
        print("Usage: python dicValidator.py input_file")
        sys.exit(1)

    filepath = sys.argv[1]
    repeated_strings, invalid_strings = find_repeated_strings(filepath)

    print("Repeated Strings:")
    if repeated_strings:
        for string, (line_numbers, iteration) in repeated_strings.items():
            print(f"String: {string}")
            print(f"  Iteration: {iteration}")
            for line_num in line_numbers:
                print(f"  Found in line {line_num}")
    else:
        print("No repeated strings found.")

    print("\nInvalid Strings:")
    if invalid_strings:
        for string, line_num in invalid_strings:
            print(f"Invalid string '{string}' found in line {line_num}")
    else:
        print("No invalid strings found.")

    print("\nSummary:")
    print(f"Number of Repeated Strings: {len(repeated_strings)}")
    print(f"Number of Invalid Strings: {len(invalid_strings)}")

if __name__ == '__main__':
    main()
