import bpy
from bpy.props import *
from bpy.types import PropertyGroup

def delFaces(self, context):
    mytool = context.scene.my_tool

    if mytool.delFaces:
        mytool.keepFaces = False
        mytool.addVertex = False

def keepFaces(self, context):
    mytool = context.scene.my_tool

    if mytool.keepFaces:
        mytool.delFaces = False
        mytool.addVertex = False

def addVertex(self, context):
    mytool = context.scene.my_tool

    if mytool.addVertex:
        mytool.delFaces = False
        mytool.keepFaces = False

class QT_settings(PropertyGroup):
    delFaces: BoolProperty(
        name = "Delete Faces",
        description = "Subdivide edges and delete adjacent faces\n(for manual restoration to avoid non-planar faces)",
        update = delFaces,
        default = True)

    keepFaces: BoolProperty(
        name = "Keep Faces",
        description = "Subdivide edges and keep adjacent faces\n(resulting faces might be non-planar)",
        update = keepFaces,
        default = False)

    addVertex: BoolProperty(
        name = "Add Vertex",
        description = "Add a vertex only",
        update = addVertex,
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
