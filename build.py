"""
Build script for creating wheel distribution.
"""
import os
import subprocess
import shutil

def clean_build():
    """Clean build directories."""
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

def build_wheel():
    """Build wheel distribution."""
    # Clean previous builds
    clean_build()
    
    # Build wheel
    subprocess.run(['python', '-m', 'build', '--wheel'], check=True)
    
    print("\nWheel file created successfully!")
    print("You can find it in the 'dist' directory.")

if __name__ == "__main__":
    build_wheel() 