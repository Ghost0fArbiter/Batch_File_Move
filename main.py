import os
import shutil
import easygui
from pathlib import Path

logfile = {}
runonce = 0
extensions = []
# GUI Creation
source = easygui.diropenbox("Pick Source folder")
destination = easygui.diropenbox("Pick Destination")
# ExtensionLower = easygui.enterbox("Please enter lowercase version only of extension \nNOTE: Does not support entering multiple extensions \nBUT Entering '*' can be used to move all files in selected directory ", "Enter the desired extension to move")
# ExtensionUpper = ExtensionLower.upper()
Extension = easygui.multchoicebox("Choose File Extensions to Move: ", "Available Extensions :) ", extensions,preselect=None)


for path in Path(source).rglob('*'):
    # splits the directory from the filename and ext
    head, tail = os.path.split(path)
    name, ext = os.path.splitext(tail)
    if ext not in extensions:
        extensions.append(ext)
Extension = easygui.multchoicebox("Choose File Extensions to Move: ", "Available Extensions :) ", extensions,
                                  preselect=None)
    #checks for the desired extension
    # if ExtensionLower != "*":
    #     if tail.endswith((ExtensionLower, ExtensionUpper)):
    #         if os.path.exists(destination + "\\"):
    #             shutil.move(path, destination + "\\" + tail)
    #             logfile[path] = destination + "\\" + tail
    # else:
    #     if os.path.exists(destination + "\\"):
    #         shutil.move(path, destination + "\\" + tail)
    #         logfile[path] = destination + "\\" + tail
while ext in extensions():
    current = extensions.pop(0)
    print(current)
if runonce == 0:
    with open('Log.txt', 'a') as Logdata:
        for k in logfile.items():
            Logdata.write('* {} has been relocated\n'.format(k))
    runonce += 1
# print("All files with Extension " + str(Extension) + " have been moved to " + str(destination))
if ExtensionLower == "*":
    easygui.msgbox("All files in " + str(source) + " and its subdirectories have been moved to " + str(destination))
else:
    easygui.msgbox("All files with Extension " + str(ExtensionLower + "," + ExtensionUpper ) + " have been moved to " + str(destination), "Notified of Change")