"""
Given a desired set of component names, this will iterate the gh document and flag with an orange
warning handler all the components you desire to find. This can be usefull when looking through
a large canvas and you need to identify components by name

    Input:
        ComponentNames: Full name of components you want to flag with a warning {list,str}
        Run: Run the script {item,bool}
    Output:
        out: Message with found components
    Remarks:
        Author: Karim Daw
        License: Apache License 2.0
        Version: 250823
"""

ghenv.Component.Name = "FindComponentsByName"
ghenv.Component.NickName = "FCBN"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Utilities"

import rhinoscriptsyntax as rs
import Grasshopper as gh
from System.Drawing import PointF

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


# Make GH component warning handler
wh = gh.Kernel.GH_RuntimeMessageLevel.Warning

@log_function(ghenv.Component.Name, csv_path)
def findComponentByName(component_names):
    component_count = {}  
    
    try:
        # Loop through all components
        for obj in ghenv.Component.OnPingDocument().Objects:
            for cmpName in component_names:
                if obj.Name == cmpName:
                    component_count[cmpName] = component_count.get(cmpName, 0) + 1
                    obj.AddRuntimeMessage(wh, "Hello! You found me!")
                    gh.Instances.ActiveCanvas.Viewport.Zoom = 10.0
                    bound = obj.Attributes.Bounds
                    gh.Instances.ActiveCanvas.Viewport.MidPoint = PointF(bound.X + bound.Width *0.5, bound.Y + bound.Height * 0.5)

        for name, count in component_count.items():
            print("I found {} component(s) with the name: {}".format(count, name))
    except Exception as e:
        print("An error occurred:", str(e))

if Run and ComponentNames:
    findComponentByName(ComponentNames)


