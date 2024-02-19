import bpy
import ctypes # import to make  dll calls and another bunch of system stuff
from bpy.app.handlers import persistent   # the script stay active even if new blend file is loaded

# https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
#ES_CONTINUOUS = 0x80000000 # a continuous flag, not needed here
#ES_SYSTEM_REQUIRED = 0x00000001 # reset standby timer
#ES_DISPLAY_REQUIRED = 0x00000002 # reset display timeout timer (and standby timer)

@persistent
def check_animation_status():
    if bpy.context.screen.is_animation_playing:
        #print("Animation is playing.")
        ctypes.windll.kernel32.SetThreadExecutionState(0x00000002) # reset the windows standby timer
    #else:
        #print("Animation is stopped.")
    return 10.0

@persistent
def scene_loaded_handler(scene):
    bpy.app.timers.register(check_animation_status)

def register():
    if not scene_loaded_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(scene_loaded_handler)
    
def unregister():
    if scene_loaded_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(scene_loaded_handler)