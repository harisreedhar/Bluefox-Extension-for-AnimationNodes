import bpy
from animation_nodes.ui.node_menu import insertNode

class BluefoxExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_bluefox_extension_menu"
    bl_label = "Bluefox Extension Menu"

    def draw(self, context):
        layout = self.layout
        layout.menu("AN_MT_Colors_menu", text = "Color")
        layout.menu("AN_MT_Effectors_menu", text = "Effectors")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    layout.separator()
    layout.menu("AN_MT_bluefox_extension_menu", text = "Bluefox Extension Menu", icon = "MESH_MONKEY")

class ColorMenu(bpy.types.Menu):
    bl_idname = "AN_MT_Colors_menu"
    bl_label = "Colors Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ColorComposite", "Color Composite")

class EffectorMenu(bpy.types.Menu):
    bl_idname = "AN_MT_Effectors_menu"
    bl_label = "Effectors Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_Inheritanceffector", "Inheritance Effector")
        insertNode(layout, "an_StepEffector", "Step Effector")
        insertNode(layout, "an_TargetEffector", "Target Effector")
        insertNode(layout, "an_TimeEffector", "Time Effector")

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
