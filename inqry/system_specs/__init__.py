import sys

OS = sys.platform

if OS == 'win32':
    import wmi
    from inqry.system_specs import windows_system_profiler as system_profiler
    from inqry.system_specs import windisk as diskutility
elif OS == 'darwin':
    from inqry.system_specs import mac_system_profiler as system_profiler
    from inqry.system_specs import macdisk as diskutility
else:
    raise OSError('Operating system unknown')




