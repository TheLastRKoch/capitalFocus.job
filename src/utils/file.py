from pathlib import Path


def get_unique_filepath(filepath: str) -> Path:
    """
    Generate a unique file path by appending a counter if the file already exists.

    Args:
        filepath (str): The initial desired file path.

    Returns:
        Path: A path object ensuring the path does not already exist.
    """
    path = Path(filepath)

    if not path.exists():
        return path

    parent_directory = path.parent
    filename_stem = path.stem
    extension = path.suffix

    counter = 1
    while True:

        new_filename = f"{filename_stem}{counter}{extension}"
        new_filepath = parent_directory / new_filename

        if not new_filepath.exists():
            return new_filepath

        counter += 1


def write(path, content):
    with open(path, 'w') as file:
        file.write(content)
