import os
import sys
# import json

class CLI_Graphics:
    operating_system = "unknown"

    class Buffer:
        buffer = [] # Every line is stored as string value in this list.

        def type_out():
            CLI_Graphics.clear(False)

            limit = len(CLI_Graphics.Buffer.buffer)
            ax = 0

            while True:
                if ax > limit:
                    break
                
                print(CLI_Graphics.Buffer.buffer[ax])


    def __init__():
        if sys.platform in ["linux", "linux2"]:
            CLI_Graphics.operating_system = "linux"
        elif sys.platform == "darwin":
            CLI_Graphics.operating_system = "os-x"
        elif sys.platform == "win32":
            CLI_Graphics.operating_system = "windows"
        else:
            input("Failed to detect operating system! cli-graphics will not work properly!")
            return
        
        """
        with open("json/cli-graphics_characters.json", "r") as characters:
            CLI_Graphics.Characters = json.load(characters)
        """

        CLI_Graphics.clear()

    
    def clear(including_buffer = True):
        if including_buffer:
            CLI_Graphics.Buffer.buffer = []
            CLI_Graphics.Buffer.type_out()

            return
        
        if CLI_Graphics.operating_system in ["linux", "os-x"]:
            return os.system("clear")
        elif CLI_Graphics.operating_system == "windows":
            return os.system("cls")