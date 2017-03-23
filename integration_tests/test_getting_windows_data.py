from inqry.system_specs import windows_system_profiler as wsp
from inqry.system_specs.systemspecs import SystemSpecs


def test_creating_a_windows_system_profile():
    return wsp.collector()


def test_hardware_function_returns_dictionary():
    assert isinstance(wsp.collector(), dict)


def test_getting_windows_internal_storage():
    assert isinstance(wsp.get_internal_storage(), list)


def test_creating_a_system_specs_object_from_collector_function():
    return SystemSpecs(test_creating_a_windows_system_profile())


def test_system_specs_storage_method_returns_dictionary():
    ss = test_creating_a_system_specs_object_from_collector_function()
    assert isinstance(ss.storage, dict)
