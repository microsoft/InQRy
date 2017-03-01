from inqry.system_specs import mac_system_profiler as sp
from inqry.system_specs import systemspecs

if __name__ == '__main__':
    ss = systemspecs.mac_os()
    print(ss.cpu_name)
    print(sp.hardware())
