import bpy
from bpy.types import Operator

def add_vertex_to_intersection(self, context): pass
def ground_objects(self, context): pass

class QT_SectEdges_Operator(Operator):
    bl_idname = "view3d.sect_edges"
    bl_label = "Intersect Edges"
    bl_description = "Intersects two edges\n(check at least one option)"
    
    def execute(self, context):
        add_vertex_to_intersection(self, context)
        return {'FINISHED'}

class QT_GroundObjects_Operator(Operator):
    bl_idname = "view3d.ground_objects"
    bl_label = "Ground Objects"
    bl_description = "Grounds objects to zero Z"
    
    def execute(self, context):
        ground_objects(self, context)
        return {'FINISHED'}

def add_vertex_to_intersection(self, context):
    obj = bpy.context.object

    if obj.mode != 'EDIT':
        self.report({"WARNING"}, "Works in edit mode only")
        return

    me = obj.data
    bm = bmesh.from_edit_mesh(me)
    edges = [e for e in bm.edges if e.select]

    if len(edges) != 2:
        self.report({"WARNING"}, "Select two edges")
        return

    mytool = context.scene.my_tool

    [[v1, v2], [v3, v4]] = [[v.co for v in e.verts] for e in edges]

    iv = geometry.intersect_line_line(v1, v2, v3, v4)
    iv = (iv[0] + iv[1]) / 2

    if mytool.delFaces_bool:
        bm.verts.new(iv)
        bm.verts.ensure_lookup_table()
        vn = bm.verts[-1]	

        for e in edges:
            bm.edges.new((e.verts[0], vn))
            bm.edges.new((e.verts[1], vn))
            bm.edges.remove(e)

    elif mytool.keepFaces_bool:
        fac = (iv - v1).length / (v2 - v1).length
        bmesh.utils.edge_split(edges[0], edges[0].verts[0], fac)

        fac = (iv - v3).length / (v4 - v3).length
        bmesh.utils.edge_split(edges[1], edges[1].verts[0], fac)

        bm.verts.ensure_lookup_table()
        bmesh.ops.pointmerge(bm, verts=[bm.verts[-1], bm.verts[-2]], merge_co=iv)

    bmesh.update_edit_mesh(me)

    if mytool.setCursor_bool:
        context.scene.cursor.location = iv

def ground_objects(self, context):
    if not len(context.selected_objects):
        self.report({"WARNING"}, "No object(s) selected")
        return        

    for obj in context.selected_objects:
        mx = obj.matrix_world
        minz = min((mx @ v.co).z for v in obj.data.vertices)
        mx.translation.z -= minz
