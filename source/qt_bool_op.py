import bpy
from bpy.props import *
from bpy.types import PropertyGroup

def delFaces(self, context):
    mytool = context.scene.my_tool

    if mytool.delFaces:
        mytool.keepFaces = False

    return

def keepFaces(self, context):
    mytool = context.scene.my_tool

    if mytool.keepFaces:
        mytool.delFaces = False

    return

class QT_settings(PropertyGroup):
    delFaces: BoolProperty(
        name = "Delete Faces",
        description = "Deletes adjacent faces\n(for manual restauration)",
        update = delFaces,
        default = True)

    keepFaces: BoolProperty(
        name = "Keep Faces",
        description = "Adds vertices to adjacent faces",
        update = keepFaces,
        default = False)

    setCursor: BoolProperty(
        name = "Set Cursor",
        description = "Sets 3D Cursor to intersection",
        default = False)

#     my_int: IntProperty(
#         name = "Set a value",
#         description="A integer property",
#         default = 23,
#         min = 10,
#         max = 100)

#     my_float: FloatProperty(
#         name = "Set a value",
#         description = "A float property",
#         default = 23.7,
#         min = 0.01,
#         max = 30.0)
