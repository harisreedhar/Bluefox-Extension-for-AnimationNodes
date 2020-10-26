import bpy
from animation_nodes.ui.node_menu import insertNode

class BluefoxExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_bluefox_extension_menu"
    bl_label = "Bluefox Extension Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SverchokInterfaceNode", "Sverchok Interface")
        insertNode(layout, "an_SimpleDeformNode", "Simple Deform")
        insertNode(layout, "an_SwitchListElementsNode", "Switch List Elements")
        insertNode(layout, "an_RigidBodyTrigger", "Rigid Body Trigger")
        insertNode(layout, "an_MarchingCubes", "Marching Cubes")
        insertNode(layout, "an_BMeshSmoothNode", "BMesh Smooth")
        insertNode(layout, "an_DupliInstancer", "Dupli Instancer")
        insertNode(layout, "an_splinetracer", "Spline Tracer")
        insertNode(layout, "an_MemoryNode", "Memory Node")
        insertNode(layout, "an_Memoryfalloff", "Memory Falloff")
        insertNode(layout, "an_NormalizeFloatsNode", "Normalize Floats")
        layout.menu("AN_MT_Colors_menu", text = "Color")
        layout.menu("AN_MT_Effectors_menu", text = "Effectors")
        layout.menu("AN_MT_extrafalloffs_menu", text = "Extra Falloffs")
        layout.menu("AN_MT_Miscellaneous_menu", text = "Miscellaneous")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    layout.separator()
    layout.menu("AN_MT_bluefox_extension_menu", text = "Bluefox Nodes", icon = "MESH_MONKEY")

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

class ExtrafalloffsMenu(bpy.types.Menu):
    bl_idname = "AN_MT_extrafalloffs_menu"
    bl_label = "Extra falloffs Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_Formulafalloff", "Formula Falloff")
        insertNode(layout, "an_RadialFalloff_old", "Radial Falloff(old)")
        insertNode(layout, "an_wavefalloff", "Wave falloff")

class MiscellaneousMenu(bpy.types.Menu):
    bl_idname = "AN_MT_Miscellaneous_menu"
    bl_label = "Miscellaneous Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_CurlNoise", "Curl Noise")
        insertNode(layout, "an_Spherical_spiral", "Spherical spiral")
        insertNode(layout, "an_fibonacci", "Fibonacci")
        insertNode(layout, "an_lorenz", "Lorenz Attractor")                

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
