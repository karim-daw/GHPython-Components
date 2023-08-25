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
    
    

    
    # loop through all components
    for obj in ghenv.Component.OnPingDocument().Objects:
        
        # set variables
        counter = 0
        foundName = "Null"
        
        for i, cmpName in enumerate(ComponentNames):
            
            # check if names match
            if obj.Name == cmpName:
                
                # enumerate counter
                counter += 1
                counter += i
                
                foundName = obj.Name
                
                obj.AddRuntimeMessage(wh,"Heloooo You found me!")  
                    
    print("I found {} components with the name: {}".format(counter, foundName))


