import yaml
import subprocess


__system_profile_data__ = None


data_types = ['hardware', 'software', 'storage']


class SubprocessCheckOutput(object):
    """docstring for SubprocessCheckOutput."""
    def __init__(self, arg):
        super(SubprocessCheckOutput, self).__init__()
        self.arg = arg



class SystemProfiler(object):
    """docstring for SystemProfiler."""
    def __init__(self, data_type=None):
        if data_type is None:
            raise TypeError("Must call method on SystemProfiler")
        super(SystemProfiler, self).__init__()
        self.output = subprocess.check_output(
            ['/usr/sbin/system_profiler',
             'SP' + data_type.title() + 'DataType'])

    def hardware(self):
        data_type = 'hardware'
        hardware = yaml.load(self.output)['Hardware']['Hardware Overview']
        print(self.data_type)
        return data_type

    def storage(self):
        self.data_type = 'storage'
        storage = yaml.load(self.output)['Storage']
        return storage

sp = SystemProfiler()


#
#     output = subprocess.check_output(
#         ['/usr/sbin/system_profiler', 'SP' + data_type.title() + 'DataType'])
#     hardware = yaml.load(output)['Hardware']['Hardware Overview']
#     return hardware
#
#
# def get_system_profiler_data(data_type):
#     if data_type not in data_types:
#         raise TypeError('Invalid data type: {}'.format(data_type))
#     else:
#         hardware = get_hardware(data_type)
#         storage = get_storage(data_type)
#         return data
