"""
Write main component documentation here.
    Inputs:
        Toggle: {item,system.object}
        InflateBox: {item,system.object}
        Geometry: {item,geometrybase}
    Outputs:
        Result: 
    Remarks:
        Author: Anders Holden Deleuran (BIG IDEAS)
        Project:
        License:
        Rhino: 6.23.20055.13111
        Version: 200326
"""

ghenv.Component.Name = "ZoomToGeometry"
ghenv.Component.NickName ="ZTG"
ghenv.Component.Category = "FWDT-Tools"
ghenv.Component.SubCategory = "Display"

#test

import Rhino as rc

def zoomSelected(geometryBase,inflateFactor):
    
    """ Zoom to geometryBase ala Grasshopper Zoom function, inflate to zoom out """
    
    bb = geometryBase.GetBoundingBox(True)
    bb.Inflate(inflateFactor)
    avp = rc.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewport
    result = avp.ZoomBoundingBox(bb)
    
    return result

if Toggle and Geometry:
    Result = zoomSelected(Geometry,InflateBox)