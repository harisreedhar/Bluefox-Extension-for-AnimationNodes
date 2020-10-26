import bpy
from bpy.props import *
from collections import defaultdict
from . test_utils import addOneList
from animation_nodes.base_types import AnimationNode

class AddOneListNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_AddOneList"
    bl_label = "Add One List"

    def create(self):
        self.newInput("Float List", "Values", "values")
        self.newOutput("Float List", "Values", "valuesOut")

    def execute(self, values):
        return addOneList(values)
