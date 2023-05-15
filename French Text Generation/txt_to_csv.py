import csv
import sys
# Set up the input and output file paths
input_file = sys.argv[1]
output_file = sys.argv[1][:-3] + 'csv'

# Open the input file and read its lines
with open(input_file, 'r') as f:
    lines = f.readlines()

# Open the output file and write the lines as a CSV column
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for line in lines:
        writer.writerow([line.strip()])