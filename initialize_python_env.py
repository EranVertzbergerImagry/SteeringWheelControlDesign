# %% Import libraries
import os
import sys
import subprocess
import pkg_resources


def initialize_environment():
    # Adjust the path to include the parent directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    sys.path.insert(0, parent_dir)
   
    # check if the required packages are installed and install them if not
    pre_required_install_check()
    print('finished')

def pre_required_install_check():
    """
    Checks if the required packages are installed and installs them if not.
    """
    packages = ['pandas', 'matplotlib', 'numpy', 'scipy', 'control']

    for package_name in packages:
        try:
            pkg_resources.get_distribution(package_name)
        except pkg_resources.DistributionNotFound:
            print(f"{package_name} is not installed. Installing now...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
 
# Initialize the environment
initialize_environment()