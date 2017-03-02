# import sys

# if sys.platform == 'win32':
#     import win32_sysinfo as sysinfo
# elif sys.platform == 'darwin':
#     import mac_sysinfo as sysinfo
# elif 'linux' in sys.platform:
#     import linux_sysinfo as sysinfo
# etc

<<<<<<< Updated upstream
# imports
=======
def main():
    specs = sp.hardware()
    print(specs)
    jspecs = json.dumps(specs, sort_keys=True, indent=4)
    print(jspecs)
    disks = md.get_all_physical_disks()
    print(disks)
>>>>>>> Stashed changes

# descriptions

<<<<<<< Updated upstream
__author__ = "Eric Hanko, Jacob Zaval, Michael Brown"
__copyright__ = "Copyright 2017, Microsoft Corporation"
__credits__ = ["Eric Hanko", "Jacob Zaval", "Michael Brown"]
__license__ = "MIT"
__email__ = "apxlab@microsoft.com"
__status__ = "Alpha"
=======
if __name__ == '__main__':
    main()
>>>>>>> Stashed changes
