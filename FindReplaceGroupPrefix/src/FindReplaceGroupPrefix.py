
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
        Version: 230824
"""

ghenv.Component.Name = "FindReplaceGroupPrefix"
ghenv.Component.NickName = "FRGP"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Automation"


import rhinoscriptsyntax as rs
import Grasshopper.Kernel.Special as gks


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



