"""
Colors the groups in the Grasshopper document based on the provided parameters.

    Inputs:
        GroupNames: List of group names to match and assign colors.
        NamesIgnore: List of group names to ignore and not assign colors.
        Colors: List of colors corresponding to group names.
        DefaultColor: Default color to assign if a group name doesn't match.
        Run: Boolean that runs the script
    Outputs:
        Null
    Remarks:
        Author: Karim Daw (Gensler DT)
        License: Apache License 2.0
        Version: 230825
"""

ghenv.Component.Name = "GroupComponentsByColor"
ghenv.Component.NickName = "GCBC"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Automation"


import rhinoscriptsyntax as rs
import Grasshopper.Kernel.Special as gks

# logging imports
import os
import csv
import time
import datetime
import System.Environment as env

# loggig path
csv_path = r'C:\Users\43310\OneDrive - Gensler\gh_scripts\_tracker\logging.csv'

# define logging function
def log_function(script_name, csv_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            start_time = time.time()
            result = None
            error_message = None

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error_message = str(e)
            end_time = time.time()

            runtime = end_time - start_time
            current_time = datetime.datetime.now()
            username = env.UserName

            file_exists = os.path.exists(csv_path)
            with open(csv_path, mode='ab') as csv_file:
                csv_writer = csv.writer(csv_file)
                if not file_exists:
                    print(error_message)
                    csv_writer.writerow(["Script Name", "Timestamp", "Runtime", "Username", "Error"])
                csv_writer.writerow([script_name, current_time, runtime, username, error_message])
                
            # close file
            csv_file.close()
            
            return result
        return wrapper
    return decorator
    

@log_function(ghenv.Component.Name, csv_path)
def colorGroups(groupNames, namesIgnore, colors, defaultColor):

    doc = ghdoc
    for obj in ghenv.Component.OnPingDocument().Objects:
        
        # if not a group, continue loop 
        if not isinstance(obj, gks.GH_Group):
            continue
        
        # get the group object and its name and assume color will be changed
        group = obj
        groupName = group.NickName.ToString()
        changeColor = True
        
        # Check if groupName is to be ignored
        for compareName in namesIgnore:
            if compareName in groupName.lower():
                changeColor = False
        
        # means the group is to be ignore so dont change, continue loop
        if not changeColor:
            continue
        
        # chooses min number between group names and colors if they differ 
        for i in range(min(len(groupNames), len(colors))):
            compareName = groupNames[i]
            if compareName in groupName.lower():
                group.Colour = colors[i]
                break # exit if match is found
            else:
                group.Colour = defaultColor
    print("Grouped components successfully!")

if not Run:
    print("Not running")
else:
    colorGroups(GroupNames, NamesIgnore, Colors, DefaultColor)

