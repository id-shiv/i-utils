# import required packages
import subprocess

def run(command: str):
    """ Run a dos command and get the output
    """
    pass

def __install_msi(msi_path: str):
    """ Install MSI and block execution until it completes
    """
    subprocess.call(f"msiexec /i {msi_path} /qn", shell=True)