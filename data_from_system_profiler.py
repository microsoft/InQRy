import sys
import os

sys.path.append(os.path.abspath('../../../../mbu/modules'))
from Infrastructure.InfraTi.Client.Environment.system_profiler import SystemProfiler


def get_system_info_from_datatype(type_of_data):
    try:
        data = SystemProfiler().profile_for_data_type(
            ['SP' + type_of_data + 'DataType'])
        print(data)
        return data
    except TypeError:
        pass
