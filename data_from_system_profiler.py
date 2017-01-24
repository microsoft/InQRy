import sys
import os

sys.path.append(os.path.abspath('../../../../mbu/modules/Infrastructure'))
from InfraTi.Client.Environment.system_profiler import SystemProfiler


def system_info_for_datatype(type_of_data):
    try:
        data = SystemProfiler().profile_for_data_type(
            ['SP' + type_of_data + 'DataType'])
        return data
    except TypeError:
        pass
