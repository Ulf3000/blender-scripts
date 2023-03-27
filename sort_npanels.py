# Helper script to trigger update on the simple tabs addon  https://chippwalters.gumroad.com/l/simpletabs
# everytime the workspace is switched. Put this in your blender scripts startup folder

import bpy
from bpy.app.handlers import persistent   # the script stay active even if new blend file is loaded

@persistent
def update_sidebar():
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    bpy.ops.simpletabs.refresh() # refresh simple tabs addon
    bpy.ops.simpletabs.update()

@persistent
def scene_loaded_handler(scene):
    
    # create generic object() as handle
    handle = object()
    
    # subscribe to the workspace change event
    workspace_subscribe_to = bpy.types.Window, "workspace"
    bpy.msgbus.subscribe_rna(
        key=workspace_subscribe_to,
        owner=handle,
        args=(),
        notify=update_sidebar,
    )

    # subscribe to the active object change event
    object_subscribe_to = bpy.types.LayerObjects, "active"
    bpy.msgbus.subscribe_rna(
        key=object_subscribe_to,
        owner=handle,
        args=(),
        notify=update_sidebar,
    )

    # subscribe to the mode change event
    mode_subscribe_to = bpy.types.Object, "mode"
    bpy.msgbus.subscribe_rna(
        key=mode_subscribe_to,
        owner=handle,
        args=(),
        notify=update_sidebar,
    )
    
    # publish an initial event to trigger the update_sidebar function
    bpy.msgbus.publish_rna(key=workspace_subscribe_to)
    bpy.msgbus.publish_rna(key=object_subscribe_to)
    bpy.msgbus.publish_rna(key=mode_subscribe_to)

def register():
    if not scene_loaded_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(scene_loaded_handler)
    
def unregister():
    if scene_loaded_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(scene_loaded_handler)