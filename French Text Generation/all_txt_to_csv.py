import os
import fnmatch
import csv

# Define the directory to search and the file extension to match
search_dir = '../dev-clean/'
file_ext = '*.txt'
output_file = 'all_text.csv'

# Recursively search for all files with the specified extension
input_files = []
for root, dirnames, filenames in os.walk(search_dir):
    for filename in fnmatch.filter(filenames, file_ext):
        input_files.append(os.path.join(root, filename))

# For every .txt file
with open(output_file, 'w', newline='') as out_f:
    for input_file in input_files:
        # Open the input file and read its lines
        with open(input_file, 'r') as f:
            lines = f.readlines()

        # Open the output file and write the lines as a CSV column
            writer = csv.writer(out_f)
            for line in lines:
                writer.writerow([line.strip()])