from inqry.system_specs import system_profiler
from inqry.system_specs import systemspecs


def test_hardware_function_returns_dictionary():
    assert system_profiler.collector()


def test_get_internal_storage_is_list():
    assert system_profiler.get_internal_storage()


def test_instatiating_systemspecs_instance():
    assert systemspecs.SystemSpecs()
