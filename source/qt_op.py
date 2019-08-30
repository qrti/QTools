import bpy
import bmesh
from bpy.types import Operator
from mathutils import geometry

def sectEdges(self, context): pass
def groundObjects(self, context): pass
def originToSel(self, context): pass
def pointOnEdge(point, edge): pass

class QT_SectEdges_Operator(Operator):
    bl_idname = "view3d.sect_edges"
    bl_label = "Intersect Edges"
    bl_description = "Intersects two edges\n(check at least one option)"

    def execute(self, context):
        sectEdges(self, context)
        return {'FINISHED'}

class QT_GroundObjects_Operator(Operator):
    bl_idname = "view3d.ground_objects"
    bl_label = "Ground Objects"
    bl_description = "Grounds objects to zero Z"

    def execute(self, context):
        groundObjects(self, context)
        return {'FINISHED'}

class QT_OriginToSel_Operator(Operator):
    bl_idname = "view3d.origin_to_sel"
    bl_label = "Origin to Selection"
    bl_description = "Sets object origin to current selection"

    def execute(self, context):
        originToSel(self, context)
        return {'FINISHED'}

def sectEdges(self, context):
    obj = bpy.context.object

    if obj.mode != 'EDIT':
        self.report({"INFO"}, "Works in edit mode only")
        return

    me = obj.data
    bm = bmesh.from_edit_mesh(me)
    edges = [e for e in bm.edges if e.select]

    if len(edges) != 2:
        self.report({"INFO"}, "Select exactly two edges")
        return

    mytool = context.scene.my_tool

    [[v1, v2], [v3, v4]] = [[v.co for v in e.verts] for e in edges]

    if v1==v3 or v1==v4 or v2==v3 or v2==v4:
        self.report({"INFO"}, "Edges are not independent")
        return

    iv = geometry.intersect_line_line(v1, v2, v3, v4)   

    if not iv:
        self.report({"INFO"}, "Edges do not intersect")
        return

    iv = (iv[0] + iv[1]) / 2

    if not pointOnEdge(iv, v1, v2) or not pointOnEdge(iv, v3, v4):
        self.report({"WARNING"}, "Intersection not on edges")

    if mytool.delFaces:
        vn = bm.verts.new(iv)

        for e in edges:
            bm.edges.new((e.verts[0], vn))
            bm.edges.new((e.verts[1], vn))
            bm.edges.remove(e)

        bmesh.update_edit_mesh(me)

    elif mytool.keepFaces:
        fac = (iv - v1).length / (v2 - v1).length
        ev1 = bmesh.utils.edge_split(edges[0], edges[0].verts[0], fac)

        fac = (iv - v3).length / (v4 - v3).length
        ev2 = bmesh.utils.edge_split(edges[1], edges[1].verts[0], fac)

        bmesh.ops.pointmerge(bm, verts=(ev1[1], ev2[1]), merge_co=iv)

        bmesh.update_edit_mesh(me)

    if mytool.setCursor:
        context.scene.cursor.location = obj.matrix_world @ iv
    
def groundObjects(self, context):
    if not len(context.selected_objects):
        self.report({"INFO"}, "No object(s) selected")
        return

    for obj in context.selected_objects:
        mx = obj.matrix_world
        minz = min((mx @ v.co).z for v in obj.data.vertices)
        mx.translation.z -= minz

def originToSel(self, context):
    obj = bpy.context.object

    if obj.mode != 'EDIT':
        self.report({"INFO"}, "Works in edit mode only")
        return

    me = obj.data
    bm = bmesh.from_edit_mesh(me)
    
    if not True in [v.select for v in bm.verts]:
        self.report({"INFO"}, "Nothing selected")
        return   

    # cp = bpy.context.scene.cursor.location        location is stored but

    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.mode_set()
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    bpy.ops.object.mode_set(mode='EDIT')

    # bpy.context.scene.cursor.location = cp        restauration does not work

def pointOnEdge(p, v1, v2): 
    minx = min(v1[0], v2[0])
    maxx = max(v1[0], v2[0])

    miny = min(v1[1], v2[1])
    maxy = max(v1[1], v2[1])

    minz = min(v1[2], v2[2])
    maxz = max(v1[2], v2[2])

    return p[0]<=maxx and p[0]>=minx and p[1]<=maxy and p[1]>=miny and p[2]<=maxz and p[2]>=minz
