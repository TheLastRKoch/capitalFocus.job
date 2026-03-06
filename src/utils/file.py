from pathlib import Path


def get_unique_filepath(filepath: str) -> Path:
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
