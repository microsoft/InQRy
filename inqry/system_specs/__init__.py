import sys

if sys.platform == 'win32':
    from inqry.system_specs import windows_system_profiler as system_profiler
elif sys.platform == 'darwin':
    from inqry.system_specs import mac_system_profiler as system_profiler
    from inqry.system_specs import macdisk
else:
    raise OSError('Operating system unknown')
