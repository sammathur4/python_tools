import os
import re


def rename_files(folder_path):
    print("Run")
    files = os.listdir(folder_path)

    for filename in files:
        # Extract the numeric part from the filename
        match = re.search(r"Part-(\d+)", filename)
        if match:
            numeric_part = match.group(1)
            # Construct the new filename with the numeric part moved to the beginning
            new_filename = (
                f"Part-{numeric_part}_{filename.replace(f'Part-{numeric_part}', '')}"
            )
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(os.path.join(folder_path, filename), new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")


# Example usage:
folder_path = r"E:\Saksham\Languages\New Folder"
rename_files(folder_path)
