import bpy
from bpy.props import *
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )

def delFacesFunc(self, context):
    mytool = context.scene.my_tool

    if(mytool.delFaces_bool == True):   
        mytool.keepFaces_bool = False

    return

def keepFacesFunc(self, context):
    mytool = context.scene.my_tool

    if(mytool.keepFaces_bool == True):   
        mytool.delFaces_bool = False

    return

class QT_settings(PropertyGroup):
    delFaces_bool = BoolProperty(
        name = "Delete Faces",
        description = "Deletes adjacent faces\n(for manual restauration)",
        update = delFacesFunc,
        default = True
        )

    keepFaces_bool = BoolProperty(
        name = "Keep Faces",
        description = "Adds vertices to adjacent faces",
        update = keepFacesFunc,
        default = False
        )

    setCursor_bool = BoolProperty(
        name = "Set Cursor",
        description = "Sets 3D Cursor to intersection",
        default = False
        )

#     my_int = IntProperty(
#         name = "Set a value",
#         description="A integer property",
#         default = 23,
#         min = 10,
#         max = 100
#         )

#     my_float = FloatProperty(
#         name = "Set a value",
#         description = "A float property",
#         default = 23.7,
#         min = 0.01,
#         max = 30.0
#         )
