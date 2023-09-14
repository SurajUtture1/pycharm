import subprocess

try:
    process = subprocess.Popen(['systeminfo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("SystemInformation")
        print(stdout)

    else:
        print(f"Command failed with exit code: {process.returncode}")
        print("Error output:", stderr)

except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")