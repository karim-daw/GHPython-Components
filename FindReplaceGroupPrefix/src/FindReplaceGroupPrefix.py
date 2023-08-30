
"""
Colors the groups in the Grasshopper document based on the provided parameters.

    Inputs:
        FindPrefix: String indicating which prefix you're looking for in groups.
        ReplacePrefix: String indicating what prefix you want to replace with
        Run: Boolean that runs the script
    Outputs:
        Null
    Remarks:
        Author: Karim Daw (Gensler DT)
        License: Apache License 2.0
        Version: 230830
"""

ghenv.Component.Name = "FindReplaceGroupPrefix"
ghenv.Component.NickName = "FRGP"
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
csv_path = r'\\Gensler.ad\Offices\London\Committees\Design Technology Studio\4_Computation\ScriptTracker\_ghCmpTracker\logging.csv'

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
def findReplacePrefix(find_prefix, replace_prefix):

    doc = ghdoc
    
    for obj in ghenv.Component.OnPingDocument().Objects:
        
        # if not a group, continue loop 
        if not isinstance(obj, gks.GH_Group):
            continue
            
        # get the group object and assume name will be changed
        group = obj
        groupName = group.NickName.ToString()
        
        # check if groupName has prefix in "Find"
        if FindPrefix in groupName.lower():
            group.NickName = group.NickName.replace(FindPrefix, ReplacePrefix)

if not Run:
    print("Not running")
else:
    findReplacePrefix(FindPrefix, ReplacePrefix)



