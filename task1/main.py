import os
import shutil
import argparse

def copy_files_recursively(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        if os.path.isdir(src_path):
            copy_files_recursively(src_path, dest_dir)
        else:
            file_extension = os.path.splitext(item)[1][1:] or 'no_extension'
            dest_path = os.path.join(dest_dir, file_extension)
            os.makedirs(dest_path, exist_ok=True)
            shutil.copy2(src_path, dest_path)

def main():
    parser = argparse.ArgumentParser(description="Recursively copy files to new directories based on file extensions")
    parser.add_argument('src_dir', help="Path to the source directory")
    parser.add_argument('dest_dir', nargs='?', default='dist', help="Path to the destination directory (default: dist)")
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    if not os.path.isdir(src_dir):
        print(f"Source directory {src_dir} does not exist or is not a directory")
        return

    try:
        copy_files_recursively(src_dir, dest_dir)
        print(f"Files successfully copied from {src_dir} to {dest_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()