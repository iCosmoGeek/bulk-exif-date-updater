"""
Bulk update EXIF 'Date taken' (DateTimeOriginal) for JPG files based on filename.

Usage:
1. Place exiftool.exe in this folder or add it to your PATH.
2. Run this script with Python 3.
3. All .jpg files matching the pattern 'YYYY-MM-DDTHHMMSS...' will have their EXIF date set accordingly.

Author: Your Name
License: MIT
"""

import os
import re
import subprocess

# Folder containing the JPG files. Update folder path
folder = r"c:\media"
# Regex pattern to match the filename format 'YYYY-MM-DDTHHMMSS...'
pattern = re.compile(r"^(\d{4})-(\d{2})-(\d{2})T(\d{6})")

modified_count = 0

# Iterate over files in the specified folder
for filename in os.listdir(folder):
    # Process only JPG files
    if filename.lower().endswith(".jpg"):
        match = pattern.match(filename)
        # If filename matches the pattern
        if match:
            year, month, day, timestr = match.groups()
            hour, minute, second = timestr[:2], timestr[2:4], timestr[4:6]
            # Create the date string for EXIF
            date_str = f"{year}:{month}:{day} {hour}:{minute}:{second}"
            filepath = os.path.join(folder, filename)
            # Call exiftool to set DateTimeOriginal
            cmd = [
                "exiftool.exe",  # Assumes exiftool.exe is in the same folder or in PATH
                f"-DateTimeOriginal={date_str}",
                "-overwrite_original",
                filepath
            ]
            try:
                # Execute the command
                subprocess.run(cmd, check=True)
                print(f"Updated {filename} to {date_str}")
                modified_count += 1
            except Exception as e:
                print(f"Failed to update {filename}: {e}")

# Print the total number of modified files
print(f"\nTotal files modified: {modified_count}")
