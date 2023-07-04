"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "karimd"
__version__ = "2023.04.12"


ghenv.Component.Name = "GithubStatusAndCommit"
ghenv.Component.NickName = "GSAC"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Automation"

import subprocess

if Folder and ToggleGitStatus:
    directory_path = r"{}".format(Folder)

    # Check Git status
    status_command = 'cmd /k "cd {} && git status"'.format(directory_path)
    subprocess.Popen(status_command)
    
if Folder and ToggleGitFetch:
    directory_path = r"{}".format(Folder)

    command = 'cmd /k "cd {} && git fetch"'.format(directory_path)
    subprocess.Popen(command)

if Folder and ToggleGitPull:
    directory_path = r"{}".format(Folder)

    command = 'cmd /k "cd {} && git pull"'.format(directory_path)
    subprocess.Popen(command)

if Folder and ToggleGitCommit:
    commit_msg = CommitMessage # get commit message from input parameter
    directory_path = r"{}".format(Folder)

    command = 'cmd /k "cd {} && git status && git add . && git commit -m "{}""'.format(directory_path, commit_msg)
    subprocess.Popen(command)

if Folder and ToggleGitPush:
    directory_path = r"{}".format(Folder)

    command = 'cmd /k "cd {} && git push"'.format(directory_path)
    subprocess.Popen(command)




