import sys
import os

sys.path.append(os.path.abspath('../../../../mbu/modules'))
from Infrastructure.InfraTi.Client.Environment.system_profiler import SystemProfiler


datatypes = ['SPHardwareDataType', 'SPStorageDataType']


def data_from_system_profiler(datatype):
    for datatype in datatypes:
        SystemProfiler().profile_for_data_type(datatype)
