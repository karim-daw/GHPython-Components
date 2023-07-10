"""
Updates the source code of GHPython components on the canvas with the code
in the .py files in the Folder if the GHPython component Name property is 
the same as the name of one of the .py files.

    Inputs:
        CheckForUpdate: Activate the component {item,bool}
        UpdateCode: The location of the .py source code files {item,str}
        Folder: The Folder path with the latest code, can be a github repo or server link
    Outputs:
        UpdatedComponentNames: List of GHPython component names that either need to be update, or have been updated updated {list,str}
    Remarks:
        Author: Anders Holden Deleuran
        Contributor: Karim Daw
        License: Apache License 2.0
        Version: 230411
"""

ghenv.Component.Name = "UpdateGHPythonSourceCode"
ghenv.Component.NickName = "UPSC"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Automation"

import rhinoscriptsyntax as rs
import os
import Grasshopper as gh
from pprint import pprint


def getSrcCodeVersion(srcCode):
    
    """
    Attempts to get the first instance of the word "version" (or, "Version")
    in a multi line string. Then attempts to extract an integer from this line 
    where the word "version" exists. So format version YYMMDD in the GHPython 
    docstring like so (or any other integer system):
        
        Version: 160121
    """

    
    # Get first line with version in it
    srcCodeLower = srcCode.lower()
    verStr = [l for l in srcCodeLower.split('\n') if "version" in l]
    if verStr:
        
        # Get the first substring integer and return it
        verInt = [int(s) for s in verStr[0].split() if s.isdigit()]
        if verInt:
            return int(verInt[0])
    else:
        return None

def find_py_files(path):
    py_files = []
    for root, dirs, files in os.walk(path):
        if "src" in dirs:
            src_path = os.path.join(root, "src")
            for file in os.listdir(src_path):
                if file.endswith(".py"):
                    py_files.append(os.path.join(src_path, file))

    return py_files

def make_py_file_dictionary(py_files):
    srcCode = {}
    for f in pyFiles:
        fOpen = open(f)
        fRead = fOpen.read()
        filePath,fExt = os.path.splitext(f)
        splitFilePath = filePath.split("\\")
        fileName = splitFilePath[-1]
        srcCode[fileName] = fRead
    return srcCode

def checkForUpdateGHPythonSrc(srcCode, ghDocument):
    
        # Make GH component warning handler
    wh = gh.Kernel.GH_RuntimeMessageLevel.Warning
    
    # Iterate the gh canvas and update ghpython source code
    guids = []
    outOfDateComponentNames = []
    for obj in ghDocument.Objects:
        if type(obj) is type(ghenv.Component):
            if obj.Name in srcCode:
                # Check that srcCode file has higher version number than obj source code
                srcCodeVer = getSrcCodeVersion(srcCode[obj.Name])
                objSrcVer = getSrcCodeVersion(obj.Code)
                if objSrcVer and srcCodeVer > objSrcVer:
                    obj.AddRuntimeMessage(wh,"The source code of this component is out of date, consider update the code")
                    outOfDateComponentNames.append(obj.Name)

    formattedString = ""
    for s in outOfDateComponentNames:
        formattedString += "Component: {} has newer src code\n".format(s)
    return formattedString

def updateGHPythonSrc(srcCode, ghDocument):
    
        # Make GH component warning handler
    wh = gh.Kernel.GH_RuntimeMessageLevel.Warning
    
    # Iterate the gh canvas and update ghpython source code
    guids = []
    updatedComponentNames = []
    for obj in ghDocument.Objects:
        if type(obj) is type(ghenv.Component):
            if obj.Name in srcCode:

                
                # Check that srcCode file has higher version number than obj source code
                srcCodeVer = getSrcCodeVersion(srcCode[obj.Name])
                objSrcVer = getSrcCodeVersion(obj.Code)
                if objSrcVer and srcCodeVer > objSrcVer:
                    
                    # Update the obj source
                    obj.Code = srcCode[obj.Name]
                    obj.AddRuntimeMessage(wh,"GHPython code was automatically updated, input/output parameters might have changed")
                    updatedComponentNames.append(obj.Name)

                    
    formattedString = ""
    for s in updatedComponentNames:
        formattedString += "Updated {} component on canvas\n".format(s)

    ghenv.Component.AddRuntimeMessage(wh,formattedString)                  
    return formattedString

pyFiles = find_py_files(Folder)
srcCodeMap = make_py_file_dictionary(pyFiles)
if CheckForUpdate:
    UpdatedComponentNames = checkForUpdateGHPythonSrc(srcCodeMap,ghenv.Component.OnPingDocument())
if UpdateCode:
    UpdatedComponentNames = updateGHPythonSrc(srcCodeMap,ghenv.Component.OnPingDocument())
