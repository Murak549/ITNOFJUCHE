import os
import re

# Define the path of your YAML file
file_path = 'NKBK_state_names_l_english.txt'

# Check if the file exists
if os.path.exists(file_path):
    # Open the file
    with open(file_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    # Iterate over the lines
    for i in range(len(lines)):
        line = lines[i]
        # Check if the line starts with 'STATE_' and its number is greater than or equal to 909
        match = re.match(r'STATE_(\d+):', line)
        if match:
            number = int(match.group(1))
            if number >= 909:
                # Add 26 to the number part of the key
                new_number = number + 26
                lines[i] = re.sub(r'STATE_\d+:', f'STATE_{new_number}:', line)

    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
