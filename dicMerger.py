import sys
import io

def clean_entry(entry):
    return entry.split('#', 1)[0].strip()

def merge_dic_files(file1_content, file2_content):
    unique_entries = set()

    for line in file1_content.splitlines():
        cleaned_entry = clean_entry(line)
        if cleaned_entry:
            unique_entries.add(cleaned_entry)

    for line in file2_content.splitlines():
        cleaned_entry = clean_entry(line)
        if cleaned_entry:
            unique_entries.add(cleaned_entry)

    merged_output = '\n'.join(unique_entries)
    return merged_output

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python dicMerger.py input_file1 input_file2 output_file")
        sys.exit(1)

    input_file_path1 = sys.argv[1]
    input_file_path2 = sys.argv[2]
    output_file_path = sys.argv[3]

    with open(input_file_path1, "r", encoding="utf-8") as file1:
        input_content1 = file1.read()

    with open(input_file_path2, "r", encoding="utf-8") as file2:
        input_content2 = file2.read()

    merged_output = merge_dic_files(input_content1, input_content2)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(merged_output)

    print("Merge complete.")
