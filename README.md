# DictionaryTools
Dictionary tools for .dic files using Python and Batch files.

# How to use?
Modify the input and output filepaths for the merge of the dictionaries, then save and execute the batch file, you can tailor the batch file if you want different scripts to be executed as well as create your own.

# Contents
The respository includes the following list of files:

- dicMerger.py: merges two dictionaries and creates and output one removing comments and keeping the strings only.

- dicDuplicateRemover.py: removes all repeated instances of a string, keeping only the first one.

- dicInvalidRemover.py: removes all string considered invalid through the use of regular expressions, invalid strings are considered ones that have a size different from 12 characters and contain non hex characters.

- dicValidator.py: checks that there are no repeated or invalid strings in the output .dic file.

- merge_and_clean.bat: executes the previous scripts in the same order as they are defined.

Experiment with all these files at your own will.
