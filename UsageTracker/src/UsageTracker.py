"""
Sets named Boolean Toggles to False when Grasshopper file opens.
    Inputs:
        Toggles: Names of Boolean Toggles to False {list,str}
        ScriptName: (OPTIONAL) name of script you want to track, by default the
        component will take the name of the file
        Activate: Activate to allow the tracker to do its thing, for testing turning it off
    Outputs:
    Remarks:
        Author: Karim Daw
        Constributor: Anders Holden Deleuran 
        License: Apache License 2.0
        Version: 230927
"""

import Grasshopper as gh

ghenv.Component.Name = "UsageTracker"
ghenv.Component.NickName = "UT"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Tracking"

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

if not ScriptName:
    fileName = ghenv.LocalScope.ghdoc.Path.split("\\")[-1]
else:
    fileName = ScriptName

@log_function(fileName, csv_path)
def dummyFunction():
    print("Ran function")

# Make persistent variable to check if GH document has opened
if "ghDocFirstOpen" not in globals():
    ghDocFirstOpen = True

# Set all named toggles to False
if Toggles and ghDocFirstOpen and Activate:
    
    # run dummy function for tracking
    dummyFunction()
    
    for obj in ghenv.Component.OnPingDocument().Objects:
        if obj.NickName in Toggles:
            if type(obj) is gh.Kernel.Special.GH_BooleanToggle:
                obj.Value = False
                obj.ExpireSolution(True)
                
    # Set flag to false
    ghDocFirstOpen = False