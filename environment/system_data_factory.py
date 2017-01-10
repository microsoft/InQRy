from modules.Infrastructure.InfraTi.Client.Environment.system_profiler_report_data import SystemProfilerReportData
from modules.Infrastructure.InfraTi.Client.Environment.system_profiler import SystemProfiler


class SystemDataFactory:
    def __init__(self):
        pass

    @staticmethod
    def Create():
        return SystemProfilerReportData(
            SystemProfiler().profile_for_data_type(['SPHardwareDataType', 'SPDeveloperToolsDataType']))