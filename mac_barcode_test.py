import os
import sys
import inspect
import barcode
import re
import unittest

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"/Users/erichanko/Projects/AutoInfra/mbu/modules/Infrastructure/InfraTi/Client/Environment")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from system_profiler_report_data import SystemProfilerReportData
from system_profiler import SystemProfiler
