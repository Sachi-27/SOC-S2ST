import os
import fnmatch

# Define the directory to search and the file extension to match
search_dir = '../dev-clean/'
file_ext = '*.txt'

# Recursively search for all files with the specified extension
matches = []
for root, dirnames, filenames in os.walk(search_dir):
    for filename in fnmatch.filter(filenames, file_ext):
        matches.append(os.path.join(root, filename))

# Print the list of matching files
for match in matches:
    print(match)