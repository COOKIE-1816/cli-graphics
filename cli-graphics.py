import os
import sys
# import json

class CLI_Graphics:
    operating_system = "unknown"


    def __init__():
        if sys.platform in ["linux", "linux2"]:
            CLI_Graphics.operating_system = "linux"
        elif sys.platform == "darwin":
            CLI_Graphics.operating_system = "os-x"
        elif sys.platform == "win32":
            CLI_Graphics.operating_system = "windows"
        else:
            input("Failed to detect operating system! cli-graphics will not work properly!")
        
        """
        with open("json/cli-graphics_characters.json", "r") as characters:
            CLI_Graphics.Characters = json.load(characters)
        """

        CLI_Graphics.clear()