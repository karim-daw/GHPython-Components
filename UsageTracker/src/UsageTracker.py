"""
The component appends log data to a file showcasing the usage of the canvas. The
Intention is to track usage of scripts with this component

    Input:
        Activate: Boolean to activate tracking 
    Output:
        Void
    Remarks:
        Author: Karim Daw
        License: Apache License 2.0
        Version: 230822
"""
ghenv.Component.Name = "UsageTracker"
ghenv.Component.NickName = "UT"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Tracking"

import time
import os
import Grasshopper as gh


def saveUseLog(_nameOfScript, _versionNumber):
    
    """Utility for saving a log file indicating script was run."""

    # Create a new path based on current timestamp
    dir_path = r'\\Gensler.ad\Offices\London\Committees\Design Technology Studio\4_Computation\ScriptTracker\\'
    file_name = 'RhinoTemplateLog_' + str(time.strftime("%Yy%mm%dd-%Hh%Mm%Ss")) + '.txt'
    full_Path = dir_path + file_name
    if os.path.isfile(full_Path) is False:
        logData = ['Gensler FWDT script was used once at ' + str(time.strftime("%Yy%mm%dd-%Hh%Mm%Ss")) + '.']
        logData.append('ScriptName: ' + str(_nameOfScript))
        logData.append('Username: ' + str(os.getenv('username')))
        logData.append('Version: ' + str(_versionNumber))
        try:
            with open(full_Path, 'w') as logFile:
                for line in logData:
                    logFile.write(line)
                    logFile.write('\n')
                logFile.close()
                return True
        except:
            ghenv.Component.AddRuntimeMessage(error, "Unable to access Gensler Server, please contact karim_daw@gensler.com.")
            return False
        return True
    elif os.path.isfile(full_Path) is True:
        ghenv.Component.AddRuntimeMessage(error, "Failed to create unique name for log file, please try again in 10 seconds.")
        return False

# Initialize warning handler
warning = gh.Kernel.GH_RuntimeMessageLevel.Warning
error = gh.Kernel.GH_RuntimeMessageLevel.Error
remark = gh.Kernel.GH_RuntimeMessageLevel.Remark

# MAIN
if Activate:
    # run script
if saveUseLog(NameOfScript, VersionNumber) is True:
    # Place script here
    pass
