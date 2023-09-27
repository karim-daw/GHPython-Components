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
        Version: 230411
"""
ghenv.Component.Name = "ReplaceUserObjectsWithLocal"
ghenv.Component.NickName = "RUOWL"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Automation"

#this is a test

import os
import Grasshopper as gh
#import getpass
import System.Environment as env

#short variable name of component
gCN = ghenv.Component.Name

# Make GH component warning handler
wh = gh.Kernel.GH_RuntimeMessageLevel.Warning

import os
import shutil

import os
import shutil

def replace_folder(src_folder, dest_folder):
    """
    Delete all files and folders in `dest_folder` with the same name as the contents
    of `src_folder`, and then replace them with the contents of `src_folder`.
    If the files or folders do not exist in the destination directory, they are copied from the source directory.
    """
    
    wh = gh.Kernel.GH_RuntimeMessageLevel.Warning
     
    try:
        # Get a list of all files and folders in the source folder
        src_contents = os.listdir(src_folder)

        # Iterate over the contents of the destination folder
        dest_contents = os.listdir(dest_folder)
        for item in dest_contents:
            # Construct the source and destination paths for the current item
            src_path = os.path.join(src_folder, item)
            dest_path = os.path.join(dest_folder, item)

            # Skip the .git folder and its contents
            if item == ".git":
                continue

            # If the current item exists in the source folder, delete it from the destination folder
            if item in src_contents:
                if os.path.isfile(dest_path):
                    os.remove(dest_path)
                elif os.path.isdir(dest_path):
                    shutil.rmtree(dest_path)

        # Copy the contents of the source folder to the destination folder
        for item in src_contents:
            # Construct the source and destination paths for the current item
            src_path = os.path.join(src_folder, item)
            dest_path = os.path.join(dest_folder, item)

            # If the current item is a file, copy it to the destination folder
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_path)

            # If the current item is a folder, recursively replace its contents in the destination folder
            elif os.path.isdir(src_path):
                # Skip the .git folder and its contents
                if item == ".git":
                    continue

                # Create the destination folder if it does not exist
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)

                # Recursively replace the contents of the current folder in the destination folder
                replace_folder(src_path, dest_path)

        formattedString = "Contents of {} replaced successfully.".format(dest_folder)
        print(formattedString)
        ghenv.Component.AddRuntimeMessage(wh,formattedString)    

    except Exception as e:
        # Handle any exceptions that might occur
        print("Error replacing contents of {}: {}".format(dest_folder, str(e)))



if Toggle and LocalFolder:
    
    # Get user name
    #print(env.UserName)
    # username=getpass.getuser()
    username = env.UserName

    # get local GH componenet folder
    localGhFolder = "C:\\Users\\"+username+"\\AppData\\Roaming\\Grasshopper\\UserObjects\\"
    replace_folder(LocalFolder,localGhFolder)
   
    

