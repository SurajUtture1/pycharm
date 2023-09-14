import os

import subprocess

command = "dir"  # Replace this with your desired Windows command
result = subprocess.run(command, shell=True, text=True, capture_output=True)

print("Exit Code:", result.returncode)
print("Standard Output:", result.stdout)
print("Standard Error:", result.stderr)