"""
Iterates the GHPython components in the document and makes user objects of them
if the their Category property matches the input Category parameter. Also grabs
all the code and writes this to .py files.

    Input:
        Toggle: Activate the component using a boolean toggle {item,bool}
        Folder: The folder/directory to save the user objects and source code to {item,str}
        Category: The name of the category for which to make user objects {item,str}
    Output:
        TLOC: Lines of code in user object {item,int}
    Remarks:
        Author: Anders Holden Deleuran
        Contributor: Karim Daw
        License: Apache License 2.0
        Version: 230704
"""
ghenv.Component.Name = "GHPythonToUserObject"
ghenv.Component.NickName = "PTUO"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Automation"

import os
import Grasshopper as gh
#import getpass
import System.Environment as env

#short variable name of component
gCN = ghenv.Component.Name

# Make GH component warning handler
wh = gh.Kernel.GH_RuntimeMessageLevel.Warning

def ghPythonToUserObject(ghPyComp,writeFolder):
    
    """ 
    Automates the creation of a GHPython user object. Based on this thread:
    http://www.grasshopper3d.com/forum/topics/change-the-default-values-for-userobject-popup-menu
    """
    
    # Make a user object
    uo = gh.Kernel.GH_UserObject()
    
    # Set its properties based on the GHPython component properties
    uo.Icon = ghPyComp.Icon_24x24    
    uo.BaseGuid = ghPyComp.ComponentGuid
    uo.Exposure = ghenv.Component.Exposure.primary
    uo.Description.Name = ghPyComp.Name
    uo.Description.Description = ghPyComp.Description
    uo.Description.Category = ghPyComp.Category
    uo.Description.SubCategory = ghPyComp.SubCategory
    
    # Set the user object data and save to file
    uo.SetDataFromObject(ghPyComp)
    uo.Path = os.path.join(writeFolder,ghPyComp.Name+".ghuser")
    uo.SaveToFile()
    
    # Update the grasshopper ribbon UI (doesn't seem to work)
    gh.Kernel.GH_ComponentServer.UpdateRibbonUI()

def exportGHPythonSource(ghPyComp,writeFolder):
    
    """ Export the source code of a GHPython component """
    
    # Get code and lines of code
    code = ghPyComp.Code
    code = code.replace("\r","")
    lines = code.splitlines()
    loc = len(lines)
    
    # Check/make source file folder
    srcFolder = os.path.join(writeFolder,"src")
    if not os.path.isdir(srcFolder):
        os.makedirs(srcFolder)
        
    # Write code to .py file
    srcFile = os.path.join(srcFolder,ghPyComp.Name + ".py")
    f = open(srcFile,"w")
    f.write(code)
    f.close()
    
    return loc

def saveGhComponent(obj,folder):
    
    ghPythonToUserObject(obj,folder)
    loc = exportGHPythonSource(obj,folder)
    obj.AddRuntimeMessage(wh,"I was just saved as a user object, hooray!")    

def get_user_from_environment():
    a = str(os.path.expanduser('~'))
    a_ls = os.path.split(a)
    return a_ls[-1]


if Toggle and LocalFolder and Category:
    
    # Get user name
    print(env.UserName)
    # username=getpass.getuser()
    username = get_user_from_environment()

    # get local GH componenet folder
    localGhFolder = "C:\Users\\"+username+"\AppData\Roaming\Grasshopper\UserObjects"

    # Iterate the canvas and get to the GHPython components
    TLOC = 0
    for obj in ghenv.Component.OnPingDocument().Objects:

        if type(obj) is type(ghenv.Component):
            
            # Check that category matches and export to files
            if obj.Category == Category:
                
                saveGhComponent(obj,localGhFolder+"\\"+obj.Name)
                saveGhComponent(obj,LocalFolder+"\\"+obj.Name)