import re
import yaml
import subprocess


serial = subprocess.check_output(['system_profiler', 'SPSerialATADataType'])
storage = subprocess.check_output(['system_profiler', 'SPStorageDataType'])
hardware = subprocess.check_output(['system_profiler', 'SPHardwareDataType'])
