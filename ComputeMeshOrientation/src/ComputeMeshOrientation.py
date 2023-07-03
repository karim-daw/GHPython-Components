"""
Template for the creation of user objects for the Big Sustainability tab.
This text shows up as the component's description. In order to create an icon,
drag+drop 24x24 pixel png onto component. Save them under L:\TOOLS\SOURCECODE\Icons


    Inputs:
        A: This is how to create a tool tip for par A.
    Outputs:
        B: This is how to create a tool tip for par B.
    Remarks:
        Author: Karim Daw
        License: Apache License 2.0
        Version: 230629
"""

import time
import math
import Rhino.Geometry as rg


ghenv.Component.Name = "ComputeMeshOrientation"
ghenv.Component.NickName = "CMO"
ghenv.Component.Category = "KD-Tools"
ghenv.Component.SubCategory = "Mesh"


# If you want to give the component a version number etc.
ghenv.Component.Message = time.strftime(
    "%d/%m/%Y") + "\n" + time.strftime("%H:%M:%S")


def arcTanToDegrees(arcTan):
    """converts arcTangents to degrees to two decimals places"""
    degree = (arcTan * 180) / math.pi
    degree = round(degree, 2)
    return degree


arcTangents = []
orientationCategories = {}
for i, m in enumerate(Mesh):

    # explicitly compute normals
    m.Normals.ComputeNormals()
    m.FaceNormals.ComputeFaceNormals()

    faceNormals = m.FaceNormals
    for j, norm in enumerate(faceNormals):
        xNorm = norm.X
        yNorm = norm.Y
        arctan = math.atan2(xNorm, yNorm)
        arctan = round(arctan*100)/100.0
        degrees = round(math.degrees(arctan))

        if abs(norm.Z) > 1 or abs(norm.Z) < 1:

            if abs(arctan) == 3.14:
                arctan = 3.14
                arcTangents.append(arctan)
            else:
                arcTangents.append(arctan)


ArcTangents = arcTangents
Orientations = map(arcTanToDegrees, arcTangents)
print(Orientations)
