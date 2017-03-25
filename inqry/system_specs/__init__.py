import sys

OS = sys.platform

if OS == 'win32':
    from inqry.system_specs import windows_system_profiler as system_profiler
elif OS == 'darwin':
    from inqry.system_specs import mac_system_profiler as system_profiler
else:
    raise OSError('Operating system unknown')
