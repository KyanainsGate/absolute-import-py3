import sys
import pathlib
import os

PKGS = ["child"]  # Set child modules
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir))
[sys.path.append(os.path.join(str(current_dir), pkg)) for pkg in PKGS]
