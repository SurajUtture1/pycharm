import subprocess


def run_command(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Command:", ' '.join(command))
            print("Output:")
            print(stdout)
        else:
            print(f"Command {' '.join(command)} failed with exit code: {process.returncode}")
            print("Error output:", stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")


# Get OS information
run_command(['wmic', 'os', 'get', 'Caption,CSDVersion,OSArchitecture'])

# Get processor information
run_command(['wmic', 'cpu', 'get', 'Name,MaxClockSpeed,NumberOfCores'])

# Get memory information
run_command(['wmic', 'memorychip', 'get', 'Capacity,DeviceLocator,Speed'])