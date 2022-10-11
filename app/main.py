### NKA Development Organization 2022. For enquiries, contact <pybotdevs@outlook.com> ###

# Imports
import os
import os.path
import pwd
import corelibs.colors
from utils.autodirectory import make_directory
from threading import Thread
import guis.settings

# Config
version = "2022.927.1"
wdir = os.getcwd()
pid = os.getpid()
host = os.uname()[1]
user = pwd.getpwuid(os.getuid())[0]
errcode = None

# Initialize Lib Modules
color = corelibs.colors.Stdout()


# Core Functions
def fdate(timestamp):
    return timestamp.strftime("%m/%d/%Y, %H:%M:%S")


# Functions
def start():
    if version is None or version == "":
        print(f"==> {color.yellow}WARNING - No version was found in app configuration{color.end}")
        print(f"PyTerm - Beta Release [no version] {color.yellow}(Unstable){color.end}")
    else: print(f"PyTerm - Beta Release v{version} {color.yellow}(Unstable){color.end}")
    print(f"Running as PID: {pid}")
    make_directory(user)


def listen_for_command(errorcode):
    if errorcode is None or errorcode == 0: cmd = input(f"{color.cyan}{user}{color.end}@{color.blue}{host}{color.end} <{wdir}> % ")
    else: cmd = input(f"{color.red}{errorcode}{color.end} {color.cyan}{user}{color.end}@{color.blue}{host}{color.end} <{wdir}> % ")
    rescode = None
    if cmd.lower() == "exit": exit(0)
    elif cmd.lower() == "settings": open_window("settings")
    else: rescode = os.system(cmd)
    return rescode


def cleanup():
    """Cleans up the environment of all variables"""
    if errcode is not None: del errcode
    if wdir is not None: del wdir
    if pid is not None: del pid
    if host is not None: del host
    if user is not None: del user
    if color is not None: del color


def open_window(window_name: str):
    if window_name == "settings":
        window = Thread(target=guis.settings.run)
        window.start()


# Initialization
start()
while True:
    try:
        errcode = listen_for_command(errcode)
    except KeyboardInterrupt:
        print("Keyboard Interrupt initialized. Cleaning up...")
        cleanup()
        exit(130)
