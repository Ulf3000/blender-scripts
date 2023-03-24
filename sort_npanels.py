# Helper script to trigger update on the simple tabs addon  https://chippwalters.gumroad.com/l/simpletabs
# everytime the workspace is switched. Put this in your blender scripts startup folder

import bpy
from bpy.app.handlers import persistent   # the script stay active even if new blend file is loaded

@persistent
def update_sidebar(context):
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",context.workspace.name)
    bpy.ops.simpletabs.refresh() # refresh simple tabs addon
    bpy.ops.simpletabs.update()

@persistent
def scene_loaded_handler(scene):
    # create generic object() as handle
    handle = object()
    # subscribe to the workspace change event
    subscribe_to = bpy.types.Window, "workspace"
    bpy.msgbus.subscribe_rna(
        key=subscribe_to,
        owner=handle,
        args=(bpy.context,),
        notify=update_sidebar,
    )
    
    # publish an initial event to trigger the update_sidebar function
    bpy.msgbus.publish_rna(key=subscribe_to)

def register():
    if not scene_loaded_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(scene_loaded_handler)
    
def unregister():
    if scene_loaded_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(scene_loaded_handler)