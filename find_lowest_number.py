# The script will find the lowest number in a file and write it to another file.
#
# Run as: python3 find_lowest_number.py <input_file> <output_file>
#
# Example: python3 find_lowest_number.py numbers.txt lowest_number.txt
#
# If python is setup to run as "python" instead of "python3" on the machine, 
# then we should use "python" instead of "python3" in the above.
#
# The input file should contain one number per line. The output file will 
# contain the lowest number.
#
# If the input file is blank, the output file will contain the text: "No 
# numbers found in file".

import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

number_found = False

with open(input_filename, 'r') as input_file:
    for line in input_file:
        if number_found == False:
            try:
                lowest_number = float(line)
                number_found = True
            except ValueError:
                break
        else:
            if float(line) < lowest_number:
                lowest_number = float(line)

with open(output_filename, 'w') as output_file:
    if number_found:
        output_file.write(str(lowest_number) + "\n")
    else:
        output_file.write("No numbers found in file\n")