# Bulk EXIF 'Date taken' Updater

This script updates the EXIF 'Date taken' (DateTimeOriginal) property for all JPG files in a folder, based on the date and time in their filenames.

## Features
- Parses filenames in the format: `YYYY-MM-DDTHHMMSS...`
- Sets the EXIF 'Date taken' to match the date and time in the filename
- Uses [exiftool](https://exiftool.org/) for robust metadata editing

## Requirements
- Python 3
- [ExifTool](https://exiftool.org/) (Download and place `exiftool.exe` in this folder or add it to your PATH)

## Usage
1. Download [ExifTool for Windows](https://exiftool.org/) and extract `exiftool(-k).exe`. Rename it to `exiftool.exe` and place it in this folder or add it to your PATH.
2. Run the script with Python 3:
   ```sh
   python update_date_taken.py
   ```
3. The script will print a summary of how many files were updated.

## Example
For a file named `2025-06-16T171408-990Z_940846347.jpg`, the EXIF 'Date taken' will be set to `2025:06:16 17:14:08`.

## License
MIT
