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


# Function to check initial lines
def checkInitialLines(string):
    if string.startswith('pm_'):
        return True

    elif string.startswith('default_building_'):
        return True
    
    elif string.startswith('automatic_irrigation_building_'):
        return True
    
    else:
        return False
    
# Function to replace initial lines
def replaceInitialLines(string):
    if string.startswith('pm_'):
        string0 = string.replace('pm_', '')
        return string0
    
    elif string.startswith('default_building_'):
        string0 = string.replace('default_building_', 'default_')
        return string0
    
    elif string.startswith('automatic_irrigation_building_'):
        string0 = string.replace('automatic_irrigation_building_', 'automatic_irrigation_')
        return string0

# Function to get the production methods
def getProductionMethods(file_name):

    # Define the file name
    file_to_open = path + file_name

    # Create a list of rows
    rows = []

    # Define the column names
    columns = ["pm", "trade_good", "value"]

    # Import the text file with the encoding
    with open(file_to_open, 'r', encoding = 'utf-8-sig') as file:
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
            if checkInitialLines(key):
                pm = replaceInitialLines(key)
        
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

    # Return data frame
    return(df)

df_industry = getProductionMethods(file_names[1])
df_industry

df_agro = getProductionMethods(file_names[2])
df_agro

df_mines = getProductionMethods(file_names[3])
df_mines

df_plantations = getProductionMethods(file_names[4])
df_plantations

df_military = getProductionMethods(file_names[5])
df_military

df_urban_center = getProductionMethods(file_names[6])
df_urban_center

df_government = getProductionMethods(file_names[7])
df_government

df_misc_resource = getProductionMethods(file_names[9])
df_misc_resource

df_private_infrastructure = getProductionMethods(file_names[11])
df_private_infrastructure

df_subsistence = getProductionMethods(file_names[12])
df_subsistence

df_construction = getProductionMethods(file_names[13])
df_construction

### Task: include sector name