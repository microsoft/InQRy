import os
from plistlib import readPlistFromString
from subprocess import Popen, PIPE


class SystemProfiler:
    def __init__(self):
        pass

    @staticmethod
    def profile_for_data_type(data_types):
        try:
            with open(os.devnull, 'w') as ignoresWrites:
                data = Popen(["/usr/sbin/system_profiler", "-xml"] + data_types, stdout=PIPE, stderr=ignoresWrites).communicate()[0]
                return readPlistFromString(data)
        except Exception as ex:
            print('InfraTi: Could not start system_profiler to collect environment info: {}'.format(ex))
            raise


