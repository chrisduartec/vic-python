import re
import pandas as pd
import os

# Describe path
path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\Victoria 3\\game\\common\\production_methods\\"



# Create a list of file names
file_names = []

# Get all file names from a directory
with os.scandir(path) as entries: # Scan through the names within the path
    for entry in entries:

        entry_name = entry.name # Get each file name

        if entry_name.endswith('.txt'): # Get if it is .txt
            file_names.append(entry_name)


# Create a function 
def getProductionMethods():
    # Create a list of rows
    rows = []

    # Define the column names
    columns = ["pm", "trade_good", "value"]

    # Import the text file with the encoding
    with open(path + '01_industry.txt', 'r', encoding = 'utf-8-sig') as file:
        content = file.readlines()

    # Define the pattern
    pattern = f"\d+"

    for line in content:

        # Check if the line starts with 'pm_' or 'building'
        if any(keyword in line for keyword in ('pm_', 'building_')):

            # Split on equal sign
            line_strip = line.strip()
            key = line_strip.split("=")[0]
        
            # Get the pm
            if key.startswith("pm_"):
                pm = key.strip()[3:]
        
            # Get input/output/employment and the trade_good
            elif key.startswith("building_"):
                if "modifiers" not in key.split("_")[1]:
                    io = key.split("_")[1]
                    trade_good = key.split("_")[2]

                    # Get the values associated with the goods
                    value_string = line_strip.split("=")[1]
                    value_init = int(re.search(pattern, value_string).group())
                
                    # If it is an input, change value to negative
                    if io == 'input':
                        value = int((-1)*value_init)
                
                    else:
                        value = value_init

                    # Append into row
                    rows.append([pm, trade_good, value])

        else:
            continue



# Create a list of rows
rows = []

# Define the column names
columns = ["pm", "trade_good", "value"]

# Import the text file with the encoding
with open(path + '01_industry.txt', 'r', encoding = 'utf-8-sig') as file:
    content = file.readlines()

# Define the pattern
pattern = f"\d+"

for line in content:

    # Check if the line starts with 'pm_' or 'building'
    if any(keyword in line for keyword in ('pm_', 'building_')):

        # Split on equal sign
        line_strip = line.strip()
        key = line_strip.split("=")[0]
        
        # Get the pm
        if key.startswith("pm_"):
            pm = key.strip()[3:]
        
        # Get input/output/employment and the trade_good
        elif key.startswith("building_"):
            if "modifiers" not in key.split("_")[1]:
                io = key.split("_")[1]
                trade_good = key.split("_")[2]

                # Get the values associated with the goods
                value_string = line_strip.split("=")[1]
                value_init = int(re.search(pattern, value_string).group())
                
                # If it is an input, change value to negative
                if io == 'input':
                    value = int((-1)*value_init)
                
                else:
                    value = value_init

                # Append into row
                rows.append([pm, trade_good, value])

    else:
        continue

# Create data frame
df = pd.DataFrame(rows, columns = columns)







