from inqry.system_specs import mac_system_profiler
from inqry.system_specs import systemspecs

SYSTEM_SPECS = systemspecs.SystemSpecs()


def test_getting_all_defined_data_types_succeeds_and_returns_a_dict():
    for data_type in mac_system_profiler.DataTypes:
        assert isinstance(mac_system_profiler.get_data(data_type), dict)


def test_hardware_function_returns_dictionary():
    assert isinstance(mac_system_profiler.collector(), dict)


def test_collector_method_output_data_type_is_system_specs_class():
    assert isinstance(SYSTEM_SPECS, systemspecs.SystemSpecs)


def test_if_disk_list_is_dict():
    assert isinstance(SYSTEM_SPECS.storage, dict)


def test_get_internal_storage_is_not_empty():
    assert len(mac_system_profiler.get_internal_storage()) > 0
