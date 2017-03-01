from inqry import system_profiler
from inqry import systemspecs

if __name__ == '__main__':
    sp = systemspecs.mac_os()
    print(sp.cpu_name)
    print(system_profiler.hardware())
