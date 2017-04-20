from inqry.system_specs import system_profiler
from inqry.system_specs import diskutility


def test_hardware_function_returns_dictionary():
    assert system_profiler.get_hardware_overview()


def test_diskutility_gets_internal_storage():
    assert diskutility.get_internal_storage()
