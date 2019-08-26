import bpy
from bpy.types import Panel

class QT_SectEdges_PT_Panel(Panel):
    bl_idname = "QT_SECT_EDGES_PT_Panel"
    bl_label = "Intersect Edges"
    bl_category = "QTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        row = layout.row()
        row.prop(mytool, 'delFaces_bool')

        row = layout.row()
        row.prop(mytool, 'keepFaces_bool')

        row = layout.row()
        row.prop(mytool, 'setCursor_bool')

        row = layout.row()
        row.operator('view3d.sect_edges', text="Intersect Edges")

class QT_GroundObjects_PT_Panel(Panel):
    bl_idname = "QT_GROUND_OBJECTS_PT_Panel"
    bl_label = "Ground Objects"
    bl_category = "QTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view3d.ground_objects', text="Ground Objects")
