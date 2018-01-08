#!/usr/bin/env python3

import platform

message = """Hello from within the container!

This container is running Python version {python_version}.
""".format(python_version=platform.python_version())

if __name__ == '__main__':
    print(message)
