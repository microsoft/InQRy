# from inqry.system_specs import mac_system_profiler
# from inqry.system_specs import systemspecs
#
# SYSTEM_SPECS = systemspecs.SystemSpecs()
#
#
# def test_getting_all_defined_data_types_succeeds_and_returns_a_dict():
#     for data_type in mac_system_profiler.DataTypes:
#         assert isinstance(mac_system_profiler.get_data(data_type), dict)
#
#
# def test_hardware_function_returns_dictionary():
#     assert mac_system_profiler.collector()
#
#
# def test_get_internal_storage_is_list():
#     assert mac_system_profiler.get_internal_storage()
#
#
# def test_instatiating_systemspecs_instance():
#     assert SYSTEM_SPECS
