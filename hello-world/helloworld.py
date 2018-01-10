#!/usr/bin/env python3
import os 
import platform

message = """Hello from within the container!

This container is running Python version {python_version} 
\nRunning file located in {file_loc}.
""".format(python_version=platform.python_version(),
           file_loc=os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    print(message)
