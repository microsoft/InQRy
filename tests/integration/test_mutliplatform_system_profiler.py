from inqry.system_specs import system_profiler
from inqry.system_specs import diskutility


def test_hardware_function_returns_dictionary():
    assert system_profiler.get_hardware_overview()


def test_diskutility_gets_internal_storage():
    assert diskutility.get_internal_storage()


def test_all_disks_return_as_internal():
    for disk in diskutility.get_internal_storage():
        assert disk.is_internal
