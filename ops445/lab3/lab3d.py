#!/usr/bin/env python3

# Author ID: [seneca_id]

import subprocess

def free_space():
    # Run the df command to get disk space information and extract the free space on the root directory
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)
    
    # Return the free space as a UTF-8 string without newline characters
    return result.stdout.strip()

# Uncomment the following line to test the function:
# print(free_space())
