# from inqry.system_specs import systemspecs
#
# DATA = {'Model Name': 'Surface_Pro_3', 'Manufacturer': 'Microsoft Corporation',
#         'Serial Number (system)': '000048250353', 'Model Identifier': 'Surface Pro 3',
#         'Number of Processors': 1, 'Total Number of Cores': 2,
#         'Processor Speed': 'Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz', 'Memory': '8 GB',
#         'Processor Name': 'Intel(R) Core(TM) i7-4650U CPU @ 1.70GHz'}
#
# SYSTEM_SPECS = systemspecs.SystemSpecs(DATA)
#
#
# def test_operating_system_attribute():
#     assert hasattr(SYSTEM_SPECS, "os_type")
#
#
# def test_that_system_profile_object_has_storage_attribute():
#     assert hasattr(SYSTEM_SPECS, "storage")
#
#
# def test_that_system_profile_object_has_serial_attribute():
#     assert hasattr(SYSTEM_SPECS, "serial")
#
#
# def test_that_system_profile_object_has_cpu_name_attribute():
#     assert hasattr(SYSTEM_SPECS, "cpu_name")
#
#
# def test_that_system_profile_object_has_cpu_speed_attribute():
#     assert hasattr(SYSTEM_SPECS, "cpu_speed")
#
#
# def test_that_system_profile_object_has_cpu_processors_attribute():
#     assert hasattr(SYSTEM_SPECS, "cpu_processors")
#
#
# def test_system_profiler_has_os_type_attribute():
#     assert SYSTEM_SPECS.os_type
#
#
# def test_model_is_string():
#     assert SYSTEM_SPECS.model
#
#
# def test_serial_is_string():
#     assert SYSTEM_SPECS.serial
#
#
# def test_name_is_string():
#     assert SYSTEM_SPECS.cpu_name
#
#
# def test_processors_is_integer():
#     assert SYSTEM_SPECS.cpu_processors
#
#
# def test_speed_is_string():
#     assert SYSTEM_SPECS.cpu_speed
#
#
# def test_cores_is_integer():
#     assert SYSTEM_SPECS.cpu_cores
