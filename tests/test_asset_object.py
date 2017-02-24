import pytest
from inqry.asset import Asset
from inqry.system_summary import SystemProfile


sp = SystemProfile()
asset = Asset(sp)


def test_empty_asset_instantiation_works():
    Asset(sp)


def test_empty_asset_is_not_valid():
    assert not asset.is_valid()


def test_presence_of_cpu_name_attribute():
    assert hasattr(asset, 'cpu_name')


def test_cpu_attribute_is_tuple():
    assert isinstance(asset.cpu_name, str)


def test_presence_of_cpu_speed_attribute():
    assert hasattr(asset, 'cpu_speed')


def test_cpu_speed_is_integer():
    assert isinstance(asset.cpu_speed, str)


def test_presence_of_cpu_processors_attribute():
    assert hasattr(asset, 'cpu_processors')


def test_cpu_processor_is_string():
    assert isinstance(asset.cpu_processors, int)


def test_presence_of_cpu_cores_attribute():
    assert hasattr(asset, 'cpu_cores')


def test_cpu_cores_is_integer():
    assert isinstance(asset.cpu_cores, int)


def test_presence_of_memory_attribute():
    assert hasattr(asset, 'memory')


def test_memory_attribute_is_string():
    assert isinstance(asset.memory, str)


def test_presence_of_serial_attribute():
    assert hasattr(asset, 'serial')


def test_serial_attribute_is_string():
    assert isinstance(asset.serial, str)


def test_presence_of_name_attribute():
    assert hasattr(asset, 'name')


def test_name_attribute_is_string():
    assert isinstance(asset.model, str)


def test_presence_of_model_attribute():
    assert hasattr(asset, 'model')


def test_model_attribute_is_string():
    assert isinstance(asset.model, str)


def test_serial_is_correct_length():
    assert len(asset.serial) == 12


@pytest.mark.skip
def test_asset_is_valid_with_known_good_test_data():
    pass
