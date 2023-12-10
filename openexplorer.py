bl_info = {
    "name": "Open Explorer",
    "description": "Adds a button to open the render output folder in Windows Explorer",
    "blender": (2, 80, 0),
    "category": "Render",
}

import bpy
import subprocess
import os

class RENDER_PT_output_explorer(bpy.types.Panel):
    bl_label = "Output Explorer"
    bl_idname = "RENDER_PT_output_explorer"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Output Path:")

        row = layout.row()
        row.prop(scene.render, "filepath", text="")

        row = layout.row()
        row.operator("render.open_explorer", text="Open Explorer")

class RENDER_OT_open_explorer(bpy.types.Operator):
    bl_idname = "render.open_explorer"
    bl_label = "Open Explorer"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        filepath = bpy.context.scene.render.filepath
        if os.path.exists(filepath):
            subprocess.Popen(['explorer', '/select,', os.path.normpath(filepath)])
        else:
            self.report({'ERROR'}, f"Path does not exist: {filepath}")

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator("render.open_explorer")

def register():
    bpy.utils.register_class(RENDER_PT_output_explorer)
    bpy.utils.register_class(RENDER_OT_open_explorer)
    bpy.types.RENDER_PT_output.append(menu_func)

def unregister():
    bpy.utils.unregister_class(RENDER_PT_output_explorer)
    bpy.utils.unregister_class(RENDER_OT_open_explorer)
    bpy.types.RENDER_PT_output.remove(menu_func)

if __name__ == "__main__":
    register()
