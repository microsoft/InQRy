class SystemProfilerReportData:
    def __init__(self, profiler_data):
        self.profiler_data = profiler_data

    @property
    def hardware(self):
        if self.profiler_data[0]['_dataType'] != 'SPHardwareDataType':
            return {}

        hardware_info = self.profiler_data[0]['_items'][0]

        output = {
            'processor_speed': hardware_info.get('current_processor_speed'),
            'machine_name': hardware_info.get('machine_name'),
            'machine_model': hardware_info.get('machine_model'),
            'boot_rom_version': hardware_info.get('boot_rom_version'),
            'cpu_type': hardware_info.get('cpu_type'),
            'l2_cache_core': hardware_info.get('l2_cache_core'),
            'l3_cache': hardware_info.get('l3_cache'),
            'number_of_processors': hardware_info.get('number_processors'),
            'physical_memory': hardware_info.get('physical_memory')
        }

        return flush_none_values_from_dict(output)

    @property
    def developer(self):
        if self.profiler_data[1]['_dataType'] != 'SPDeveloperToolsDataType' or len(
                self.profiler_data[1]['_items']) == 0:
            return {}

        items = self.profiler_data[1]['_items'][0]

        output = {}
        if 'spdevtools_apps' in items:
            dev_tools = items['spdevtools_apps']
            output = {
                'instruments_version': dev_tools.get('spinstruments_app'),
                'xcode_version': dev_tools.get('spxcode_app'),
            }

        for k, v in items['spdevtools_sdks'].iteritems():
            versions = []

            for _k, _v in v.iteritems():
                versions.append('{} {}'.format(_k, _v))
                output[k.replace('sp', '')] = ", ".join(versions)

        return flush_none_values_from_dict(output)


def flush_none_values_from_dict(dict):
    return {k: v for k, v in dict.items() if not v is None}
