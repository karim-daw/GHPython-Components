"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "43310"
__version__ = "2023.08.25"


ghenv.Component.Name = "FindComponentsByName"
ghenv.Component.NickName = "FCBN"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Utilities"

import rhinoscriptsyntax as rs
import Grasshopper as gh

# Make GH component warning handler
wh = gh.Kernel.GH_RuntimeMessageLevel.Warning

if Run and ComponentNames:
    component_count = {}  # Using a more descriptive name for the dictionary
    
    # Loop through all components
    for obj in ghenv.Component.OnPingDocument().Objects:
        for cmpName in ComponentNames:
            if obj.Name == cmpName:
                component_count[cmpName] = component_count.get(cmpName, 0) + 1
                obj.AddRuntimeMessage(wh, "Hello! You found me!")
    
    for name, count in component_count.items():
        print("I found {} component(s) with the name: {}".format(count, name))

