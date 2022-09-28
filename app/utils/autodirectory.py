### NKA Development Organization 2022. For enquiries, contact <pybotdevs@outlook.com>

# Imports
import os
import os.path
import pwd


# Config
user = pwd.getpwuid(os.getuid())[0]


# Functions
def make_directory(username: str):
    """Makes app path in user's home directory if there is no app path. If there is, this is automatically skipped."""
    default_path = f"/home/{username}"
    if not os.path.isdir(f"{default_path}/pyterm"):
        os.mkdir(f"{default_path}/pyterm")  # Making main directory
        open(f"{default_path}/pyterm/pytermrc", "x")
        os.mkdir(f"{default_path}/pyterm/history")
        open(f"{default_path}/pyterm/history/username_hist.txt", "x")
        os.mkdir(f"{default_path}/pyterm/logs")
        open(f"{default_path}/pyterm/logs/{username}_info.log", "x")
        open(f"{default_path}/pyterm/logs/{username}_error.log", "x")


# Initialization
# make_directory(user)
