import os


def list_dir_structure(base_dir, indent_level=0, exclude=None):
    """
    Recursively lists the directory structure for the specified folder, with the ability to exclude certain directories or files.

    Parameters:
    base_dir (str): The base directory to start listing.
    indent_level (int): Current level of indentation for pretty printing.
    exclude (list): List of directories or files to exclude from listing.
    """
    if exclude is None:
        exclude = []

    try:
        entries = sorted(os.listdir(base_dir))
        for entry in entries:
            if entry in exclude:
                continue
            entry_path = os.path.join(base_dir, entry)
            prefix = "  " * indent_level + "|-- "
            print(f"{prefix}{entry}")
            if os.path.isdir(entry_path):
                list_dir_structure(entry_path, indent_level + 1, exclude)
    except PermissionError:
        print("  " * indent_level + "|-- [Permission Denied]")
    except FileNotFoundError:
        print(f"[Error] Directory '{base_dir}' not found.")
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")


if __name__ == "__main__":
    current_folder = os.getcwd()
    # Add directories or files to exclude here
    exclude_list = [".git", "__pycache__"]

    print(f"Directory structure of the current folder:\n{current_folder}")
    print(f"Excluding: {', '.join(exclude_list)}")
    print()
    list_dir_structure(current_folder, exclude=exclude_list)
