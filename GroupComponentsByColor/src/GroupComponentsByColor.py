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
        Author: Karim Daw
        License: Apache License 2.0
        Version: 230710
"""

ghenv.Component.Name = "GroupComponentsByColor"
ghenv.Component.NickName = "GCBC"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Automation"


import rhinoscriptsyntax as rs
import Grasshopper.Kernel.Special as gks

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

