import os


def find_path(path_name):
    # Get the current working directory
    current_dir = os.getcwd()

    # Check if the path_name is an absolute path or a relative path
    if os.path.isabs(path_name):
        # If the path_name is already an absolute path, return it directly
        return path_name
    else:
        # If the path_name is a relative path, join it with the current working directory
        return os.path.join(current_dir, path_name)


if __name__ == "__main__":
    # Ask the user for the path name
    user_input = input("Enter the file or directory name: ")

    # Find the path
    path = find_path(user_input)

    # Check if the path exists
    if os.path.exists(path):
        print("The path to '{}' is: {}".format(user_input, path))
    else:
        print("Path not found!")
