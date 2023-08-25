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

