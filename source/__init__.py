# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "QTools",
    "author" : "qrti",
    "description" : "QTools",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.props import *

from . qt_panel   import QT_SectEdges_PT_Panel, QT_GroundObjects_PT_Panel
from . qt_op      import QT_SectEdges_Operator, QT_GroundObjects_Operator
from . qt_bool_op import QT_settings

# classes = (QT_IntersectEdges_Operator, QT_IntersectEdges_PT_Panel, QT_settings)
# register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    bpy.utils.register_class(QT_SectEdges_PT_Panel)
    bpy.utils.register_class(QT_GroundObjects_PT_Panel)
    bpy.utils.register_class(QT_SectEdges_Operator)
    bpy.utils.register_class(QT_GroundObjects_Operator)
    bpy.utils.register_class(QT_settings)
    bpy.types.Scene.my_tool = PointerProperty(type=QT_settings)

def unregister():
    bpy.utils.unregister_class(QT_SectEdges_PT_Panel)
    bpy.utils.unregister_class(QT_GroundObjects_PT_Panel)
    bpy.utils.unregister_class(QT_SectEdges_Operator)
    bpy.utils.unregister_class(QT_GroundObjects_Operator)
    bpy.utils.unregister_class(QT_settings)
    del bpy.types.Scene.my_tool
