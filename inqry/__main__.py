import shelve
import pickle
import json
from inqry.system_specs import macdisk as md
from inqry.system_specs import mac_system_profiler as sp
from inqry.system_specs import systemspecs


def main():
    specs = sp.hardware()
    print(specs)
    jspecs = json.dumps(specs, sort_keys=True, indent=4)
    print(jspecs)
    disks = md.get_all_physical_disks()
    print(disks)


if __name__ == '__main__':
    main()
