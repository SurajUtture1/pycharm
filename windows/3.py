import subprocess


def get_os_information():
    try:
        process = subprocess.Popen(['wmic', 'os', 'get', 'Caption,CSDVersion,OSArchitecture'], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("OS Information:")
            print(stdout)
        else:
            print(f"Command failed with exit code: {process.returncode}")
            print("Error output:", stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")


get_os_information()
