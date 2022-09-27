### NKA Development Organization 2022. For enquiries, contact <pybotdevs@outlook.com>

# Imports
import os
import os.path
import pwd
import time
import corelibs.colors
# import datetime
# import math

# Config
version = "0.0.1"
wdir = os.getcwd()
pid = os.getpid()
host = os.uname()[1]
user = pwd.getpwuid(os.getuid())[0]
errcode = None

# Initialize Lib Modules
colors = corelibs.colors.Stdout()

# Core Functions
def fdate(timestamp):
    return timestamp.strftime("%m/%d/%Y, %H:%M:%S")

# Functions
def start():
    if version is None or version == "":
        print(f"==> {colors.yellow}WARNING - No version was found in app configuration{colors.end}")
        print(f"PyTerm - Beta Release [no version] {colors.yellow}(Unstable){colors.end}")
    else: print(f"PyTerm - Beta Release v{version} {colors.yellow}(Unstable){colors.end}")
    print(f"Running as PID: {pid}")

def listen_for_command(errorcode):
    if errorcode is None or errorcode == 0: cmd = input(f"{colors.cyan}{user}{colors.end}@{colors.blue}{host}{colors.end} <{wdir}> % ")
    else: cmd = input(f"{colors.red}{errorcode}{colors.end} {colors.cyan}{user}{colors.end}@{colors.blue}{host}{colors.end} <{wdir}> % ")
    rescode = None
    if cmd.lower() == "exit": exit(0)
    else: rescode = os.system(cmd)
    return rescode

def cleanup():
    """Cleans up the environment of all variables"""
    del errcode
    del wdir
    del pid
    del host
    del user
    del colors


# Initialization
start()
while True:
    try:
        errcode = listen_for_command(errcode)
    except KeyboardInterrupt:
        print("Keyboard Interrupt initialized. Cleaning up...")
        cleanup()
        exit(130)
