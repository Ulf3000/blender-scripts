# blender-scripts
various scripts for blender

# sort_npanel.py 
Helper script to trigger update on the simple tabs addon  https://chippwalters.gumroad.com/l/simpletabs everytime the workspace/mode/active object is changed. 
Put this in your blender scripts startup folder. 
For best measure you should add a script folder to blender preferences. That way you dont have to do this for every new blender version and works across the board. 

![grafik](https://user-images.githubusercontent.com/10765339/227530317-f782c895-014e-403d-b622-7daf2c5e3c0f.png)



# openexplorer.py
Adds a button to open the render output folder in Windows Explorer

![grafik](https://github.com/Ulf3000/blender-scripts/assets/10765339/0122a246-be47-48e0-b47b-cee10542686e)


# preventSleep.py

prevents the pc and connected displays to go into standby/sleep mode if blender is playing. 
Now you can watch your animation in loop or your long video scene in the videoeditor and still keep a reasonable powermanagement.

Put this in your blender scripts startup folder. 

Works only on windows for now. 

For Linux and MacOS similar apis should exist, replace the line:

ctypes.windll.kernel32.SetThreadExecutionState(ES_DISPLAY_REQUIRED) # reset the windows standby timer

with whatever correct api call or a simple mousemove or shift press(anything which prevents the displays going to sleep) 
